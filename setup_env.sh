#!/bin/bash

# Create a new conda environment for book compilation
conda create -y -n books python=3.8

# Activate the environment
echo "Activating conda environment..."
eval "$(conda shell.bash hook)"
conda activate books

# Install required packages
echo "Installing required packages..."
conda install -y pandoc
pip install pyyaml markdown

echo "Environment setup complete. Run:"
echo "conda activate books"
echo "python book_compiler.py" 