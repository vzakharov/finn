#!/usr/bin/env python3
import yaml
import os
from datetime import datetime, date
from typing import Any

def load_yaml_data(yaml_path: str):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def parse_release_date(release_date_str: str):
    """Parse a release date in the format 'MMM YYYY'"""
    try:
        return datetime.strptime(release_date_str, "%b %Y").date()
    except ValueError:
        # Default to old date if parsing fails
        return date(2000, 1, 1)

def get_release_status(release_date_str: str):
    """Calculate the release status based on date"""
    today = date.today()
    release_date = parse_release_date(release_date_str)
    
    # Calculate months since release
    months_diff = (today.year - release_date.year) * 12 + today.month - release_date.month
    
    if months_diff < 6:
        return "recent"
    elif months_diff < 12:
        return "medium"
    else:
        return "old"

def generate_markdown(models: list[dict[str, Any]], output_path: str):
    md_header = "| Vendor | Model | Parameters, B | Context, k tokens | API | Open Source | Reasoning | Public | Release |\n"
    md_separator = "|--------|-------|---------------------------|---------|-----|-------------|-----------|--------|----------|\n"
    
    rows: list[str] = []
    for model in models:
        vendor = model['vendor']
        model_name = model['model']
        model_url = model['url']
        parameters = model['parameters']
        context = model['context']
        api = "✅" if model['api'] else "❌"
        open_source = "✅" if model['open_source'] else "❌"
        reasoning = "✅" if model['reasoning'] else "❌"
        
        if model['public'] == True:
            public = "✅"
        elif model['public'] == "limited":
            public = "🚧"
        else:
            public = "❌"
        
        release = model['release']
        
        # Get status based on date instead of using the field from YAML
        release_status = get_release_status(release)
        
        # Color coding for release recency in markdown
        if release_status == "recent":
            release_colored = f"🟩 {release}"
        elif release_status == "medium":
            release_colored = f"🟧 {release}"
        else:
            release_colored = f"◻️ {release}"
        
        model_link = f"[{model_name}]({model_url})"
        
        row = f"| {vendor} | {model_link} | {parameters} | {context} | {api} | {open_source} | {reasoning} | {public} | {release_colored} |\n"
        rows.append(row)
    
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_header)
        md_file.write(md_separator)
        for row in rows:
            md_file.write(row)
        
        # Add source line at the end
        md_file.write("\n\nSource: [A.I., Motherfuckers!](https://dub.sh/aimofos)\n")

def generate_html(models: list[dict[str, Any]], output_path: str):
    html_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Cheatsheet May 2025</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            color: #333;
            font-size: 11px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th {
            background-color: #a83232 !important;
            color: white !important;
            padding: 6px;
            text-align: left;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #ffe6e6 !important;
        }
        tr:nth-child(odd) {
            background-color: #fff0f0 !important;
        }
        td {
            padding: 4px;
            border: 1px solid #ddd;
        }
        a {
            color: #a83232;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .source {
            font-size: 0.8em;
            margin-top: 10px;
            text-align: right;
            color: #888;
        }
        .recent {
            color: green !important;
            font-weight: bold;
        }
        .medium {
            color: orange !important;
        }
        .old {
            color: gray !important;
        }
        @media print {
            body {
                font-size: 14px;
                margin: 0;
                padding: 0;
            }
            th {
                background-color: #a83232 !important;
                color: white !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            tr:nth-child(even) {
                background-color: #ffe6e6 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            tr:nth-child(odd) {
                background-color: #fff0f0 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            .recent, .medium, .old {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            td {
                padding: 3px;
            }
            h1 {
                font-size: 14px;
                margin: 5px 0;
            }
            .source {
                font-size: 7px;
            }
        }
    </style>
</head>
<body>
    <h1>LLM Cheatsheet - May 2025</h1>
    <table>
        <thead>
            <tr>
                <th>Vendor</th>
                <th>Model</th>
                <th>Parameters, B</th>
                <th>Context, k tokens</th>
                <th>API</th>
                <th>OS</th>
                <th>Reasoning</th>
                <th>Public</th>
                <th>Release</th>
            </tr>
        </thead>
        <tbody>
"""
    
    html_rows: list[str] = []
    for model in models:
        vendor = model['vendor']
        model_name = model['model']
        model_url = model['url']
        parameters = model['parameters']
        context = model['context']
        api = "✅" if model['api'] else "❌"
        open_source = "✅" if model['open_source'] else "❌"
        reasoning = "✅" if model['reasoning'] else "❌"
        
        if model['public'] == True:
            public = "✅"
        elif model['public'] == "limited":
            public = "🚧"
        else:
            public = "❌"
        
        release = model['release']
        
        # Calculate status based on date
        release_status = get_release_status(release)
        
        model_link = f'<a href="{model_url}" target="_blank">{model_name}</a>'
        
        row = f"""            <tr>
                <td>{vendor}</td>
                <td>{model_link}</td>
                <td>{parameters}</td>
                <td>{context}</td>
                <td>{api}</td>
                <td>{open_source}</td>
                <td>{reasoning}</td>
                <td>{public}</td>
                <td class="{release_status}">{release}</td>
            </tr>
"""
        html_rows.append(row)
    
    html_end = """        </tbody>
    </table>
    <div class="source">Source: <a href="https://dub.sh/aimofos" target="_blank">A.I., Motherfuckers!</a></div>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_start)
        for row in html_rows:
            html_file.write(row)
        html_file.write(html_end)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, 'cheatsheet.yaml')
    md_output = os.path.join(current_dir, 'cheatsheet.md')
    html_output = os.path.join(current_dir, 'cheatsheet.html')
    
    data = load_yaml_data(yaml_path)
    models = data['models']
    
    generate_markdown(models, md_output)
    generate_html(models, html_output)
    
    print(f"Generated Markdown at: {md_output}")
    print(f"Generated HTML at: {html_output}")

if __name__ == "__main__":
    main() 