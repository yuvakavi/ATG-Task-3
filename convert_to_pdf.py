"""
Convert SUBMISSION.md to PDF using markdown-pdf or weasyprint
"""
import subprocess
import sys
from pathlib import Path

def convert_with_markdown_pdf():
    """Try converting with markdown-pdf (npm package)"""
    try:
        cmd = ["markdown-pdf", "SUBMISSION.md", "-o", "SUBMISSION.pdf"]
        subprocess.run(cmd, check=True)
        print("✓ Converted using markdown-pdf")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_with_pandoc():
    """Try converting with pandoc"""
    try:
        cmd = [
            "pandoc", 
            "SUBMISSION.md",
            "-o", "SUBMISSION.pdf",
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=11pt",
            "--toc"
        ]
        subprocess.run(cmd, check=True)
        print("✓ Converted using pandoc")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_with_weasyprint():
    """Try converting with WeasyPrint (Python package)"""
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        # Read markdown
        with open("SUBMISSION.md", "r", encoding="utf-8") as f:
            md_text = f.read()
        
        # Convert to HTML
        html_text = markdown.markdown(
            md_text, 
            extensions=['tables', 'fenced_code', 'codehilite']
        )
        
        # Add CSS styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    line-height: 1.6;
                    margin: 40px;
                    font-size: 11pt;
                }}
                h1 {{ 
                    color: #2c3e50; 
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{ 
                    color: #34495e; 
                    margin-top: 30px;
                }}
                h3 {{ color: #7f8c8d; }}
                code {{ 
                    background: #f4f4f4; 
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{ 
                    background: #2c3e50; 
                    color: #ecf0f1;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                table {{ 
                    border-collapse: collapse; 
                    width: 100%; 
                    margin: 20px 0;
                }}
                th, td {{ 
                    border: 1px solid #bdc3c7; 
                    padding: 10px; 
                    text-align: left;
                }}
                th {{ 
                    background: #3498db; 
                    color: white;
                }}
                tr:nth-child(even) {{ background: #ecf0f1; }}
                .check {{ color: #27ae60; font-weight: bold; }}
                .cross {{ color: #e74c3c; font-weight: bold; }}
            </style>
        </head>
        <body>
            {html_text}
        </body>
        </html>
        """
        
        # Convert to PDF
        HTML(string=styled_html).write_pdf(
            "SUBMISSION.pdf",
            stylesheets=[CSS(string="@page { size: letter; margin: 1in; }")]
        )
        print("✓ Converted using WeasyPrint")
        return True
        
    except ImportError:
        print("⚠ WeasyPrint not installed. Install with: pip install weasyprint markdown")
        return False
    except Exception as e:
        print(f"✗ WeasyPrint conversion failed: {e}")
        return False

def main():
    print("📄 Converting SUBMISSION.md to PDF...\n")
    
    # Try different conversion methods in order of preference
    methods = [
        ("Pandoc", convert_with_pandoc),
        ("WeasyPrint", convert_with_weasyprint),
        ("markdown-pdf", convert_with_markdown_pdf),
    ]
    
    for name, method in methods:
        print(f"Trying {name}...")
        if method():
            print(f"\n✅ Successfully created SUBMISSION.pdf using {name}")
            print(f"   File size: {Path('SUBMISSION.pdf').stat().st_size / 1024:.1f} KB")
            return 0
    
    print("\n❌ All conversion methods failed!")
    print("\n📝 Manual conversion options:")
    print("   1. Install pandoc: https://pandoc.org/installing.html")
    print("      Then run: pandoc SUBMISSION.md -o SUBMISSION.pdf")
    print("   2. Install WeasyPrint: pip install weasyprint markdown")
    print("      Then run: python convert_to_pdf.py")
    print("   3. Use online converter: https://www.markdowntopdf.com/")
    print("   4. Open in VS Code and use 'Markdown PDF' extension")
    return 1

if __name__ == "__main__":
    sys.exit(main())
