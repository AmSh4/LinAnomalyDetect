#!/bin/bash

echo "Setting up LinAnomalyDetect environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install Python 3.12+."
    exit 1
fi

# Create virtual env if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

# Install requirements
pip install -r ../requirements.txt

echo "Setup complete. Activate env with 'source venv/bin/activate'."