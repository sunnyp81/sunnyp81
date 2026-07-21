import hmac
import os

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

API_KEY = os.environ.get("MCP_API_KEY", "")

_PUBLIC_PATHS = {"/", "/health", "/healthz"}


class BearerAuth(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path in _PUBLIC_PATHS:
            return await call_next(request)
        if not API_KEY:
            return JSONResponse(
                {"error": "server misconfigured: MCP_API_KEY not set"},
                status_code=500,
            )
        header = request.headers.get("authorization", "")
        if not header.startswith("Bearer "):
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        presented = header[len("Bearer ") :]
        if not hmac.compare_digest(presented, API_KEY):
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        return await call_next(request)
