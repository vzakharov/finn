#!/bin/bash

# Create a new conda environment for book compilation
conda create -y -n writing python=3.12

# Activate the environment
echo "Activating conda environment..."
eval "$(conda shell.bash hook)"
conda activate writing

# Install required packages
echo "Installing required packages..."
conda install -y pandoc
pip install pyyaml markdown

echo "Environment setup complete. Run:"
echo "conda activate writing"