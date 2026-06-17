#!/bin/bash
# SystemHeaven Framework - Unix/Linux/macOS Installation Script
# One-liner: curl -sSL https://.../install.sh | bash

set -e

echo "================================================================"
echo "🚀 SYSTEMHEAVEN FRAMEWORK v3.0 - UNIX INSTALLATION"
echo "================================================================"

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    echo "   Please install Python 3 and try again."
    exit 1
fi

echo "✅ Python 3 detected: $(python3 --version)"

# Create temporary directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download systemheaven.py
echo "📥 Downloading SystemHeaven installer..."
if command -v curl &> /dev/null; then
    curl -sSL -o systemheaven.py "https://raw.githubusercontent.com/DEIN_USERNAME/DEIN_REPO/main/systemheaven.py"
elif command -v wget &> /dev/null; then
    wget -q -O systemheaven.py "https://raw.githubusercontent.com/DEIN_USERNAME/DEIN_REPO/main/systemheaven.py"
else
    echo "❌ Error: Neither curl nor wget is available."
    exit 1
fi

# Verify download
if [ ! -f "systemheaven.py" ]; then
    echo "❌ Error: Failed to download installer."
    exit 1
fi

echo "✅ Installer downloaded successfully"

# Run installation
echo ""
python3 systemheaven.py --target-dir "$PWD/systemheaven"

# Move to final location
FINAL_DIR="$HOME/systemheaven"
if [ -d "$FINAL_DIR" ]; then
    echo "⚠️  Existing installation found at $FINAL_DIR"
    echo "   Backing up to $FINAL_DIR.backup.$(date +%s)"
    mv "$FINAL_DIR" "$FINAL_DIR.backup.$(date +%s)"
fi

mv "$PWD/systemheaven" "$FINAL_DIR"

# Cleanup
cd "$HOME"
rm -rf "$TEMP_DIR"

echo ""
echo "================================================================"
echo "✅ SYSTEMHEAVEN INSTALLATION COMPLETE"
echo "================================================================"
echo "📍 Installed at: $FINAL_DIR"
echo ""
echo "Next steps:"
echo "   cd $FINAL_DIR"
echo "   ls -la"
echo ""
echo "Packages installed:"
echo "   📦 1_Cornerstone-Methodology (Foundation)"
echo "   📦 2_Strategic-Architect (Governance)"
echo "   📦 3_DeepDrive-IIOS-Ultimate-Gigant-v3 (Implementation)"
echo ""
echo "🌟 SystemHeaven is ready to use!"
echo "================================================================"
