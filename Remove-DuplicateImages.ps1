<#
.SYNOPSIS
    Find and move content-identical duplicate image files into a _duplicates subfolder.

.DESCRIPTION
    Scans the target folder for image files, groups them by file size (cheap filter),
    then hashes the remaining candidates with SHA-256. For each set of content-identical
    duplicates, keeps the file with the earliest CreationTime and moves the rest into a
    _duplicates subfolder for review. Filename is ignored - only content matters.

.PARAMETER Path
    Folder to scan. Defaults to G:\My Drive\SunnyPatel.co.uk\Social-images.

.PARAMETER Recurse
    Also scan subfolders.

.PARAMETER DryRun
    List what would be moved without actually moving anything.

.PARAMETER DuplicatesFolder
    Name of the subfolder to move duplicates into. Default: _duplicates.

.EXAMPLE
    .\Remove-DuplicateImages.ps1 -DryRun

.EXAMPLE
    .\Remove-DuplicateImages.ps1
#>

[CmdletBinding()]
param(
    [string]$Path = 'G:\My Drive\SunnyPatel.co.uk\Social-images',
    [switch]$Recurse,
    [switch]$DryRun,
    [string]$DuplicatesFolder = '_duplicates'
)

$ErrorActionPreference = 'Stop'

$imageExtensions = @('.png','.jpg','.jpeg','.gif','.bmp','.webp','.tif','.tiff','.heic','.heif','.svg','.avif')

if (-not (Test-Path -LiteralPath $Path)) {
    Write-Error "Path not found: $Path"
    exit 1
}

$dupFolderPath = Join-Path -Path $Path -ChildPath $DuplicatesFolder

Write-Host "Scanning: $Path" -ForegroundColor Cyan
Write-Host "Recurse:  $Recurse"
Write-Host "Dry-run:  $DryRun"
Write-Host ""

$getParams = @{ LiteralPath = $Path; File = $true }
if ($Recurse) { $getParams['Recurse'] = $true }

$files = Get-ChildItem @getParams |
    Where-Object { $imageExtensions -contains $_.Extension.ToLower() } |
    Where-Object { $_.FullName -notlike (Join-Path $dupFolderPath '*') -and $_.DirectoryName -ne $dupFolderPath }

Write-Host "Found $($files.Count) image file(s)." -ForegroundColor Cyan

$sizeGroups = $files | Group-Object -Property Length | Where-Object { $_.Count -gt 1 }

if (-not $sizeGroups) {
    Write-Host "No files share a size - no duplicates possible. Done." -ForegroundColor Green
    return
}

$candidates = $sizeGroups | ForEach-Object { $_.Group }
Write-Host "$($candidates.Count) file(s) share a size with at least one other - hashing those..." -ForegroundColor Cyan

$hashed = foreach ($f in $candidates) {
    try {
        $h = (Get-FileHash -LiteralPath $f.FullName -Algorithm SHA256).Hash
        [pscustomobject]@{ File = $f; Hash = $h }
    } catch {
        Write-Warning "Could not hash $($f.FullName): $($_.Exception.Message)"
    }
}

$dupGroups = $hashed | Group-Object -Property Hash | Where-Object { $_.Count -gt 1 }

if (-not $dupGroups) {
    Write-Host "No content-identical duplicates found. Done." -ForegroundColor Green
    return
}

$totalToMove = 0
$bytesToReclaim = 0

Write-Host ""
Write-Host "Duplicate sets:" -ForegroundColor Yellow

foreach ($g in $dupGroups) {
    $sorted = $g.Group | Sort-Object -Property @{ Expression = { $_.File.CreationTime } }
    $keep   = $sorted[0].File
    $move   = $sorted | Select-Object -Skip 1 | ForEach-Object { $_.File }

    Write-Host ""
    Write-Host "  hash $($g.Name.Substring(0,16))... ($($g.Count) copies, $($keep.Length) bytes each)"
    Write-Host "    KEEP: $($keep.FullName)" -ForegroundColor Green
    foreach ($m in $move) {
        Write-Host "    MOVE: $($m.FullName)" -ForegroundColor Red
        $totalToMove++
        $bytesToReclaim += $m.Length
    }
}

Write-Host ""
Write-Host ("Summary: {0} file(s) to move, {1:N2} MB to reclaim." -f $totalToMove, ($bytesToReclaim / 1MB)) -ForegroundColor Cyan

if ($DryRun) {
    Write-Host "Dry-run - nothing was moved. Re-run without -DryRun to apply." -ForegroundColor Yellow
    return
}

if (-not (Test-Path -LiteralPath $dupFolderPath)) {
    New-Item -ItemType Directory -Path $dupFolderPath | Out-Null
    Write-Host "Created: $dupFolderPath"
}

$moved = 0
foreach ($g in $dupGroups) {
    $sorted = $g.Group | Sort-Object -Property @{ Expression = { $_.File.CreationTime } }
    $move   = $sorted | Select-Object -Skip 1 | ForEach-Object { $_.File }
    foreach ($m in $move) {
        $dest = Join-Path -Path $dupFolderPath -ChildPath $m.Name
        $i = 1
        while (Test-Path -LiteralPath $dest) {
            $base = [IO.Path]::GetFileNameWithoutExtension($m.Name)
            $ext  = [IO.Path]::GetExtension($m.Name)
            $dest = Join-Path -Path $dupFolderPath -ChildPath ("{0} ({1}){2}" -f $base, $i, $ext)
            $i++
        }
        Move-Item -LiteralPath $m.FullName -Destination $dest
        $moved++
    }
}

Write-Host ""
Write-Host "Done. Moved $moved duplicate(s) to: $dupFolderPath" -ForegroundColor Green
Write-Host "Review and delete manually once you're satisfied." -ForegroundColor Yellow
