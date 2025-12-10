
$ToolName = "cll-csv.exe"
$ToolDir = "$env:USERPROFILE\Tools"
$DownloadUrl = "https://github.com/ipsilo-eu/cll-csv/releases/download/v1.0.0/cll-csv.exe"

Write-Host "Starting installation of $ToolName for the current user..." -ForegroundColor Yellow

Write-Host "1. Creating directory $ToolDir..."
if (-not (Test-Path $ToolDir)) {
    New-Item -Path $ToolDir -ItemType Directory | Out-Null
    Write-Host "   -> Directory created."
} else {
    Write-Host "   -> Directory already exists."
}

Write-Host "2. Downloading $ToolName from GitHub..."
try {
    Invoke-WebRequest -Uri $DownloadUrl -OutFile (Join-Path $ToolDir $ToolName) -ErrorAction Stop
    Write-Host "   -> Download successful."
} catch {
    Write-Host "   -> ERROR: Failed to download the file. Check your internet connection." -ForegroundColor Red
    exit 1
}

Write-Host "3. Adding $ToolDir to the CURRENT USER's PATH..."
try {
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($currentPath -notcontains $ToolDir) {
        [Environment]::SetEnvironmentVariable("Path", "$currentPath;$ToolDir", "User")
        Write-Host "   -> User PATH successfully updated. The change will take effect in new console sessions." -ForegroundColor Green
    } else {
        Write-Host "   -> $ToolDir is already in the User PATH."
    }
} catch {
    Write-Host "   -> ERROR: Failed to update the User PATH." -ForegroundColor Red
    exit 1
}

Write-Host "`nInstallation of cll-csv is complete!" -ForegroundColor Green
Write-Host "To use 'cll-csv', please open a NEW PowerShell or Command Prompt window." -ForegroundColor Cyan
