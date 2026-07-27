"""Minimal MCP streamable-HTTP client (enough for pullers, no SDK).

Speaks JSON-RPC over a single POST endpoint, handles both plain-JSON
and SSE-framed responses, and threads the `Mcp-Session-Id` header
through follow-up calls. Used to pull data out of hosted MCP servers
(SEO Gets) from GitHub Actions, where a full MCP SDK is overkill.
"""

from __future__ import annotations

import json
from typing import Any

import httpx

PROTOCOL_VERSION = "2025-03-26"


class McpError(RuntimeError):
    pass


class McpHttpClient:
    def __init__(self, url: str, bearer_token: str, timeout: float = 60.0):
        self.url = url
        self.session_id: str | None = None
        self._next_id = 0
        self._client = httpx.Client(
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {bearer_token}",
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
            },
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "McpHttpClient":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    # -- transport ---------------------------------------------------------

    def _post(self, payload: dict[str, Any]) -> dict[str, Any] | None:
        headers = {}
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        r = self._client.post(self.url, json=payload, headers=headers)
        sid = r.headers.get("mcp-session-id")
        if sid:
            self.session_id = sid
        r.raise_for_status()
        if not r.content:
            return None
        ctype = r.headers.get("content-type", "")
        if "text/event-stream" in ctype:
            return self._last_sse_message(r.text, payload.get("id"))
        return r.json()

    @staticmethod
    def _last_sse_message(text: str, want_id: Any) -> dict[str, Any] | None:
        result = None
        for line in text.splitlines():
            if not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if not data:
                continue
            try:
                msg = json.loads(data)
            except ValueError:
                continue
            if want_id is None or msg.get("id") == want_id:
                result = msg
        return result

    # -- JSON-RPC ----------------------------------------------------------

    def request(self, method: str, params: dict[str, Any] | None = None) -> Any:
        self._next_id += 1
        payload: dict[str, Any] = {"jsonrpc": "2.0", "id": self._next_id, "method": method}
        if params is not None:
            payload["params"] = params
        msg = self._post(payload)
        if msg is None:
            raise McpError(f"empty response for {method}")
        if "error" in msg:
            raise McpError(f"{method}: {msg['error']}")
        return msg.get("result")

    def notify(self, method: str, params: dict[str, Any] | None = None) -> None:
        payload: dict[str, Any] = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            payload["params"] = params
        self._post(payload)

    # -- MCP lifecycle -----------------------------------------------------

    def initialize(self) -> dict[str, Any]:
        result = self.request(
            "initialize",
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": "hermes", "version": "1.0"},
            },
        )
        self.notify("notifications/initialized")
        return result

    def list_tools(self) -> list[dict[str, Any]]:
        tools: list[dict[str, Any]] = []
        cursor: str | None = None
        while True:
            res = self.request("tools/list", {"cursor": cursor} if cursor else {})
            tools.extend(res.get("tools", []))
            cursor = res.get("nextCursor")
            if not cursor:
                return tools

    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> Any:
        """Call a tool and unwrap its content to plain data where possible."""
        res = self.request("tools/call", {"name": name, "arguments": arguments or {}})
        if res.get("isError"):
            raise McpError(f"tool {name} errored: {_content_to_data(res)}")
        if "structuredContent" in res:
            return res["structuredContent"]
        return _content_to_data(res)


def _content_to_data(result: dict[str, Any]) -> Any:
    """Flatten MCP content blocks; parse text blocks as JSON when they are."""
    out: list[Any] = []
    for block in result.get("content", []) or []:
        if block.get("type") == "text":
            text = block.get("text", "")
            try:
                out.append(json.loads(text))
            except ValueError:
                out.append(text)
        else:
            out.append(block)
    if len(out) == 1:
        return out[0]
    return out
