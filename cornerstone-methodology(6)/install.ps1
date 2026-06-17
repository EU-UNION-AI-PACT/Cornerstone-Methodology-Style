# SystemHeaven Framework - Windows PowerShell Installation Script
# One-liner: Invoke-WebRequest -Uri "https://.../install.ps1" | Invoke-Expression

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "🚀 SYSTEMHEAVEN FRAMEWORK v3.0 - WINDOWS INSTALLATION" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan

# Check for Python
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCommand) {
    $pythonCommand = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $pythonCommand) {
    Write-Host "❌ Error: Python is required but not installed." -ForegroundColor Red
    Write-Host "   Please install Python from https://python.org and try again." -ForegroundColor Red
    exit 1
}

$pythonVersion = & $pythonCommand.Source --version
Write-Host "✅ Python detected: $pythonVersion" -ForegroundColor Green

# Create temporary directory
$tempDir = Join-Path $env:TEMP "systemheaven_install_$(Get-Random)"
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
Set-Location $tempDir

# Download systemheaven.py
Write-Host "📥 Downloading SystemHeaven installer..." -ForegroundColor Yellow
$installerUrl = "https://raw.githubusercontent.com/DEIN_USERNAME/DEIN_REPO/main/systemheaven.py"
$installerPath = Join-Path $tempDir "systemheaven.py"

try {
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath -UseBasicParsing
    Write-Host "✅ Installer downloaded successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: Failed to download installer." -ForegroundColor Red
    Write-Host "   $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Run installation
Write-Host ""
& $pythonCommand.Source $installerPath --target-dir "$tempDir\systemheaven"

# Move to final location
$finalDir = Join-Path $env:USERPROFILE "systemheaven"
if (Test-Path $finalDir) {
    Write-Host "⚠️  Existing installation found at $finalDir" -ForegroundColor Yellow
    $backupDir = "$finalDir.backup.$(Get-Date -Format 'yyyyMMddHHmmss')"
    Write-Host "   Backing up to $backupDir" -ForegroundColor Yellow
    Rename-Item $finalDir $backupDir
}

Move-Item "$tempDir\systemheaven" $finalDir

# Cleanup
Set-Location $env:USERPROFILE
Remove-Item $tempDir -Recurse -Force

Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "✅ SYSTEMHEAVEN INSTALLATION COMPLETE" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "📍 Installed at: $finalDir" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "   cd $finalDir" -ForegroundColor White
Write-Host "   dir" -ForegroundColor White
Write-Host ""
Write-Host "Packages installed:" -ForegroundColor Yellow
Write-Host "   📦 1_Cornerstone-Methodology (Foundation)" -ForegroundColor White
Write-Host "   📦 2_Strategic-Architect (Governance)" -ForegroundColor White
Write-Host "   📦 3_DeepDrive-IIOS-Ultimate-Gigant-v3 (Implementation)" -ForegroundColor White
Write-Host ""
Write-Host "🌟 SystemHeaven is ready to use!" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
