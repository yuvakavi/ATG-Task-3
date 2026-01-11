"""
Convert SUBMISSION.md to HTML for easy PDF printing from browser
"""
import markdown
from pathlib import Path

def convert_md_to_html():
    """Convert markdown to styled HTML"""
    
    # Read markdown
    with open("SUBMISSION.md", "r", encoding="utf-8") as f:
        md_text = f.read()
    
    # Convert to HTML
    html_content = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc']
    )
    
    # Create styled HTML
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ATG Task 3 - Technical Submission</title>
    <style>
        @media print {{
            @page {{ margin: 0.75in; }}
            body {{ font-size: 10pt; }}
            h1 {{ page-break-before: always; }}
            h1:first-of-type {{ page-break-before: avoid; }}
        }}
        
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            color: #333;
            background: #fff;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
            font-size: 28pt;
        }}
        
        h2 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 20pt;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 5px;
        }}
        
        h3 {{
            color: #7f8c8d;
            margin-top: 20px;
            font-size: 16pt;
        }}
        
        h4 {{
            color: #95a5a6;
            margin-top: 15px;
            font-size: 14pt;
        }}
        
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
        
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Courier New', monospace;
            color: #e74c3c;
            font-size: 9pt;
        }}
        
        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.4;
        }}
        
        pre code {{
            background: transparent;
            padding: 0;
            color: #ecf0f1;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-size: 10pt;
        }}
        
        th, td {{
            border: 1px solid #bdc3c7;
            padding: 10px;
            text-align: left;
        }}
        
        th {{
            background: #3498db;
            color: white;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background: #ecf0f1;
        }}
        
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 5px 0;
        }}
        
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        em {{
            color: #7f8c8d;
            font-style: italic;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #3498db;
            margin: 30px 0;
        }}
        
        .toc {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 20px;
            margin: 30px 0;
        }}
        
        .toc h2 {{
            margin-top: 0;
            border-bottom: none;
        }}
        
        .header-info {{
            background: #3498db;
            color: white;
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 40px;
        }}
        
        .header-info h1 {{
            color: white;
            border: none;
            margin: 0;
            font-size: 32pt;
        }}
        
        .header-info p {{
            margin: 10px 0;
            font-size: 12pt;
        }}
        
        .print-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #27ae60;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14pt;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            z-index: 1000;
        }}
        
        .print-button:hover {{
            background: #229954;
        }}
        
        @media print {{
            .print-button {{ display: none; }}
            .header-info {{ background: white; color: #2c3e50; border: 2px solid #3498db; }}
            .header-info h1 {{ color: #2c3e50; }}
        }}
        
        .check {{ color: #27ae60; font-weight: bold; }}
        .cross {{ color: #e74c3c; font-weight: bold; }}
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Print to PDF</button>
    
    {html_content}
    
    <script>
        // Add print keyboard shortcut
        document.addEventListener('keydown', function(e) {{
            if ((e.ctrlKey || e.metaKey) && e.key === 'p') {{
                e.preventDefault();
                window.print();
            }}
        }});
    </script>
</body>
</html>"""
    
    # Write HTML file
    with open("SUBMISSION.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print("✓ Created SUBMISSION.html")
    file_size = Path("SUBMISSION.html").stat().st_size / 1024
    print(f"  File size: {file_size:.1f} KB")
    print("\n📄 To create PDF:")
    print("  1. Open SUBMISSION.html in your browser")
    print("  2. Click 'Print to PDF' button (or Ctrl+P)")
    print("  3. Select 'Save as PDF' as printer")
    print("  4. Save as SUBMISSION.pdf")

if __name__ == "__main__":
    try:
        convert_md_to_html()
        print("\n✅ Conversion successful!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
