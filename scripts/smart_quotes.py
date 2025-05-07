# pyright: strict

#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path

# Placeholder constants for curly quotes
LEFT_SINGLE_QUOTE = "‘"
RIGHT_SINGLE_QUOTE = "’"
LEFT_DOUBLE_QUOTE = "“"
RIGHT_DOUBLE_QUOTE = "”"


def convert_quotes(text: str):
    # Replace apostrophes (single quotes after word boundary)
    text = re.sub(r'(\b)\'', f'\\1{RIGHT_SINGLE_QUOTE}', text)
    
    # Replace closing double quotes (preceded by word boundary or punctuation)
    text = re.sub(r'(\b[,.!?]?)\"', f'\\1{RIGHT_DOUBLE_QUOTE}', text)
    
    # Replace opening double quotes (followed by word boundary)
    text = re.sub(r'\"(\b)', f'{LEFT_DOUBLE_QUOTE}\\1', text)
    
    return text


def process_file(file_path: Path):
    """Process a single file, replacing quotes."""
    print(f"Processing: {file_path}")
    
    # Skip binary files and non-text files
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping binary file: {file_path}")
        return
    
    # Convert quotes
    new_content = convert_quotes(content)
    
    # Write back if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")


def process_directory(directory_path: str, extensions: 'list[str] | None' = None):
    """Process all files in a directory and its subdirectories."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory {directory_path} does not exist")
        return
    
    # Default extensions to process (now only .md by default)
    if extensions is None:
        extensions = ['.md']
    
    # Recursively walk through directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if extensions and file_path.suffix.lower() in extensions:
                process_file(file_path)


def main():
    parser = argparse.ArgumentParser(description='Convert straight quotes to curly quotes in text files')
    parser.add_argument('directory', help='Directory to process recursively')
    parser.add_argument('--extensions', help='Comma-separated list of file extensions to process (default: .md)')
    
    args = parser.parse_args()
    
    extensions = None
    if args.extensions:
        extensions = args.extensions.split(',')
    
    process_directory(args.directory, extensions)
    print("Processing complete!")


if __name__ == "__main__":
    main() 