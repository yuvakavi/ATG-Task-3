#!/bin/bash

# Setup script for avatar-system

echo "Setting up Real-Time Talking Avatar System..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo "✓ Setup complete!"
echo "Activate environment with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
