# Leak-scan: standardise .gitignore across all local repos
# Append-only. Idempotent. Won't touch existing rules.

$ErrorActionPreference = 'Stop'

$RequiredPatterns = @(
    '.env',
    '.env.*',
    '.env.local',
    '.env.production',
    '*.pem',
    '*.key',
    'credentials.json',
    'credentials*.json',
    'secrets.*',
    '.wrangler/',
    '.vercel/',
    '.next/cache/',
    'wordpress-config.md',
    'master-builds.md',
    'node_modules/',
    'dist/'
)

$SearchRoots = @(
    'C:\Users\sunny\repos',
    'C:\Users\sunny\projects',
    'C:\Users\sunny\Desktop'
)

$results = @()
$reposScanned = 0
$reposChanged = 0

foreach ($root in $SearchRoots) {
    if (-not (Test-Path $root)) { continue }
    $gitDirs = Get-ChildItem -Path $root -Directory -Recurse -Force -ErrorAction SilentlyContinue `
        -Filter '.git' -Depth 3 | Where-Object { $_.Name -eq '.git' }

    foreach ($gitDir in $gitDirs) {
        $repoPath = $gitDir.Parent.FullName
        $reposScanned++
        $gitignorePath = Join-Path $repoPath '.gitignore'

        $existingLines = @()
        if (Test-Path $gitignorePath) {
            $existingLines = Get-Content $gitignorePath -ErrorAction SilentlyContinue |
                ForEach-Object { $_.Trim() }
        }

        $missing = @()
        foreach ($pattern in $RequiredPatterns) {
            if ($existingLines -notcontains $pattern) {
                $missing += $pattern
            }
        }

        if ($missing.Count -gt 0) {
            $reposChanged++
            $header = ''
            if (-not (Test-Path $gitignorePath) -or (Get-Item $gitignorePath).Length -eq 0) {
                $header = "# leak-scan: standard ignores`n"
            } else {
                $header = "`n# leak-scan: appended $(Get-Date -Format 'yyyy-MM-dd')`n"
            }
            $body = ($missing -join "`n") + "`n"
            Add-Content -Path $gitignorePath -Value ($header + $body) -Encoding utf8 -NoNewline
            $results += [PSCustomObject]@{
                Repo = $repoPath.Replace('C:\Users\sunny\','')
                Added = $missing.Count
                Patterns = ($missing -join ', ')
            }
        }
    }
}

Write-Output "=== leak-scan gitignore sweep ==="
Write-Output "Repos scanned: $reposScanned"
Write-Output "Repos updated: $reposChanged"
Write-Output ""
if ($results.Count -gt 0) {
    $results | Format-Table -AutoSize -Wrap
} else {
    Write-Output "All repos already had complete .gitignore coverage. Nothing to do."
}
Write-Output ""
Write-Output "Review changes with: git -C <repo> diff .gitignore"
Write-Output "Commit when ready."
