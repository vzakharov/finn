#!/usr/bin/env python3
import yaml
import os
from typing import Any

def load_yaml_data(yaml_path: str):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def generate_markdown(models: 'list[dict[str, Any]]', output_path: str):
    md_header = "| Vendor | Model | Parameters (active / total) | Context | API | Open Source | Reasoning | Public | Release |\n"
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
        release_status = model['release_status']
        
        # Add color indicator based on release status
        if release_status == "recent":
            release_indicator = "🟩"
        elif release_status == "medium":
            release_indicator = "🟧"
        else:
            release_indicator = "🩶"
        
        model_link = f"[{model_name}]({model_url})"
        release_with_indicator = f"{release_indicator} {release}"
        
        row = f"| {vendor} | {model_link} | {parameters} | {context} | {api} | {open_source} | {reasoning} | {public} | {release_with_indicator} |\n"
        rows.append(row)
    
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_header)
        md_file.write(md_separator)
        for row in rows:
            md_file.write(row)
        
        # Add source line at the end
        md_file.write("\n\nSource: [AI.I, Motherfuckers!](dub.sh/aimofos)\n")

def generate_html(models: 'list[dict[str, Any]]', output_path: str) -> None:
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
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th {
            background-color: #a83232;
            color: white;
            padding: 10px;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #ffe6e6;
        }
        tr:nth-child(odd) {
            background-color: #fff0f0;
        }
        td {
            padding: 8px;
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
            margin-top: 20px;
            text-align: right;
            color: #888;
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
                <th>Parameters (active / total)</th>
                <th>Context</th>
                <th>API</th>
                <th>Open Source</th>
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
        release_status = model['release_status']
        
        # Add color indicator based on release status
        if release_status == "recent":
            release_indicator = "🟩"
        elif release_status == "medium":
            release_indicator = "🟧"
        else:
            release_indicator = "🩶"
        
        model_link = f'<a href="{model_url}" target="_blank">{model_name}</a>'
        release_with_indicator = f"{release_indicator} {release}"
        
        row = f"""            <tr>
                <td>{vendor}</td>
                <td>{model_link}</td>
                <td>{parameters}</td>
                <td>{context}</td>
                <td>{api}</td>
                <td>{open_source}</td>
                <td>{reasoning}</td>
                <td>{public}</td>
                <td>{release_with_indicator}</td>
            </tr>
"""
        html_rows.append(row)
    
    html_end = """        </tbody>
    </table>
    <div class="source">Source: <a href="dub.sh/aimofos" target="_blank">AI.I, Motherfuckers!</a></div>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_start)
        for row in html_rows:
            html_file.write(row)
        html_file.write(html_end)

def main() -> None:
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