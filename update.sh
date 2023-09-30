#!/bin/bash

# Function to check if a command is available
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if Python 3.9 is installed
if ! command_exists python3.9; then
  echo "Python 3.9 not found. Installing Python 3.9 using Homebrew..."
  brew install python@3.9
else
  echo "Python 3.9 is already installed."
fi

# Check if Git is installed
if ! command_exists git; then
  echo "Git not found. Installing Git using Homebrew..."
  brew install git
else
  echo "Git is already installed."
fi

# Install dependencies using pip
echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Script completed."