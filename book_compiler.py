#!/usr/bin/env python3

import os
import re
import yaml
import subprocess
import argparse
from pathlib import Path
import tempfile

def get_book_metadata(book_dir):
    """Read book metadata from book.yaml."""
    yaml_path = book_dir / "book.yaml"
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def find_chapter_files(book_dir):
    """Find all files starting with \d\d_ pattern and sort them."""
    chapters = []
    
    # Process all items in the directory
    for item in os.listdir(book_dir):
        item_path = book_dir / item
        
        # Check if it's a file with the pattern
        if item_path.is_file() and re.match(r'^\d\d_.*\.md$', item):
            chapters.append(item_path)
        
        # Check if it's a directory with the pattern
        elif item_path.is_dir() and re.match(r'^\d\d_.*', item):
            # Find markdown files inside the directory
            for subitem in sorted(os.listdir(item_path)):
                subitem_path = item_path / subitem
                if subitem_path.is_file() and subitem.endswith('.md'):
                    chapters.append(subitem_path)
    
    # Sort all found files based on their full path
    return sorted(chapters, key=lambda x: str(x))

def create_combined_markdown(book_dir, chapter_files):
    """Create a single combined markdown file with all chapters, separated by double newlines."""
    combined_file = book_dir / "compiled.md"
    
    # Collect the contents of all files
    with open(combined_file, 'w') as outfile:
        # Process the first file separately to handle frontmatter
        if chapter_files:
            with open(chapter_files[0], 'r') as f:
                content = f.read().strip()
                outfile.write(content)
            
            # Process remaining files
            for file_path in chapter_files[1:]:
                # Add double newlines between files
                outfile.write("\n\n")
                
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    outfile.write(content)
    
    print(f"Created combined markdown file: {combined_file}")
    return combined_file

def format_yaml_metadata(metadata):
    """Format metadata for proper display in HTML output."""
    # Create a properly formatted YAML metadata block
    formatted = {}
    
    if 'title' in metadata:
        formatted['title'] = metadata['title']
    
    if 'subtitle' in metadata:
        formatted['subtitle'] = metadata['subtitle']
    
    if 'authors' in metadata:
        # Format authors as a proper list
        if isinstance(metadata['authors'], list):
            formatted['author'] = metadata['authors']
        else:
            formatted['author'] = [metadata['authors']]
    
    return formatted

def compile_to_html(book_dir, metadata, chapter_files, debug=False):
    """Compile all markdown files into a single HTML using pandoc."""
    if not chapter_files:
        print("No chapter files found!")
        return False, None
    
    print(f"Found {len(chapter_files)} chapter files to compile.")
    
    # Debug: Print all chapter files
    for i, f in enumerate(chapter_files):
        print(f"{i+1}. {f}")
    
    # Create a combined markdown file
    combined_file = create_combined_markdown(book_dir, chapter_files)
    
    # Process metadata for proper display
    formatted_metadata = format_yaml_metadata(metadata)
    
    # Create a temporary YAML file for metadata
    with tempfile.NamedTemporaryFile('w', suffix='.yaml', delete=False) as tmp:
        yaml.dump(formatted_metadata, tmp)
        metadata_file = tmp.name
    
    # Set output file path in the book directory
    output_file = book_dir / "book.html"
    
    try:
        # Build pandoc command to convert to HTML
        cmd = [
            "pandoc",
            "-o", str(output_file),  # Output HTML file in book directory
            "--standalone",          # Make a standalone HTML file with header
            "--toc",                 # Add table of contents
            "--css=book_style.css",  # Reference CSS for styling
            "--metadata-file=" + metadata_file,  # Use metadata-file for better processing
            str(combined_file)       # Use the combined markdown file
        ]
        
        # Run pandoc
        print("Running pandoc to generate HTML...")
        print(f"Command: {' '.join(cmd)}")
        
        subprocess.run(cmd, check=True)
        print(f"Successfully compiled book to {output_file}")
        
        # Create a simple CSS file if it doesn't exist
        css_file = book_dir / "book_style.css"
        if not os.path.exists(css_file):
            create_default_css(css_file)
            
        return True, output_file
    
    finally:
        # Clean up temporary metadata file
        os.unlink(metadata_file)
        # We're now keeping the combined markdown file permanently as compiled.md

def create_default_css(css_path):
    """Create a simple default CSS file for the book."""
    css = """
    body {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        font-family: Georgia, serif;
        line-height: 1.6;
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #444;
        margin-top: 1.5em;
        clear: both;
    }
    h1 {
        font-size: 2.5em;
        border-bottom: 1px solid #eee;
        padding-bottom: 0.3em;
    }
    h2 {
        font-size: 2em;
        border-bottom: 1px solid #f8f8f8;
        padding-bottom: 0.2em;
    }
    h3 {
        font-size: 1.6em;
    }
    p {
        margin-bottom: 1.2em;
    }
    a {
        color: #0366d6;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    blockquote {
        border-left: 4px solid #ddd;
        padding-left: 1em;
        color: #666;
        margin-left: 0;
        margin-bottom: 1.2em;
    }
    code {
        background-color: #f6f8fa;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        font-family: monospace;
    }
    img {
        max-width: 100%;
    }
    #TOC {
        background-color: #f8f8f8;
        padding: 1em;
        margin-bottom: 2em;
        border-radius: 5px;
    }
    #TOC ul {
        list-style-type: none;
    }
    .title {
        text-align: center;
    }
    .subtitle {
        text-align: center;
        font-style: italic;
        margin-top: -10px;
        margin-bottom: 2em;
    }
    .author {
        text-align: center;
        font-weight: bold;
        margin-bottom: 2em;
    }
    h1.title {
        font-size: 3em;
        margin-bottom: 0.2em;
    }
    p.subtitle {
        font-size: 1.5em;
        margin-top: 0;
    }
    p.author {
        font-size: 1.2em;
    }
    """
    
    with open(css_path, "w") as f:
        f.write(css)
    print(f"Created default CSS file: {css_path}")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Compile a book from markdown files.')
    parser.add_argument('book_dir', nargs='?', default="dont_build_your_own/dictatorship",
                       help='Directory containing the book files (default: dont_build_your_own/dictatorship)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    return parser.parse_args()

def main():
    args = parse_arguments()
    book_dir = Path(args.book_dir)
    
    if not book_dir.exists() or not book_dir.is_dir():
        print(f"Error: Book directory '{book_dir}' does not exist or is not a directory.")
        return
    
    print(f"Using book directory: {book_dir}")
    
    print("Reading book metadata...")
    metadata = get_book_metadata(book_dir)
    
    print("Finding chapter files...")
    chapter_files = find_chapter_files(book_dir)
    
    print("Compiling book to HTML...")
    success, output_file = compile_to_html(book_dir, metadata, chapter_files, debug=args.debug)
    
    if success:
        print(f"Book '{metadata.get('title')}' successfully compiled to HTML!")
        print(f"You can view it by opening {output_file} in your browser.")
        print(f"The compiled markdown is available at {book_dir}/compiled.md")
    else:
        print("Failed to compile book.")

if __name__ == "__main__":
    main() 