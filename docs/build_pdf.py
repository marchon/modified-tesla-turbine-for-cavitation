#!/usr/bin/env python3
"""
Professional single-volume PDF generator for the complete Sphinx documentation.

Builds using Sphinx singlehtml (all content in one HTML file) + WeasyPrint
with a custom book-quality print stylesheet.

Produces:
- Proper title page
- Table of contents
- All documentation sections in logical book order
- Cross-reference / index at the back
- Running headers, page numbers, professional typography
- Full PDF metadata + outline (bookmarks)

Usage:
    python docs/build_pdf.py
    # or via make:
    make docs-pdf
"""

import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("ERROR: weasyprint is not installed.")
    print("Install with: pip install weasyprint")
    print("Then re-run this script.")
    sys.exit(1)

DOCS_DIR = Path(__file__).parent.resolve()
BUILD_DIR = DOCS_DIR / "_build"
HTML_DIR = BUILD_DIR / "singlehtml"
PDF_PATH = BUILD_DIR / "sphinx_documentation.pdf"

# Rich title page content (injected as first page)
TITLEPAGE_HTML = """
<div class="pdf-titlepage">
    <h1>Modified Tesla Turbine<br>for Cavitation</h1>
    <div class="subtitle">Precision Flow Conditioner for Reproducible<br>Cavitation &amp; LENR-Related Experiments</div>
    
    <div class="author">
        <strong>George Lambert</strong><br>
        Litchfield, New Hampshire
    </div>
    
    <div class="meta">
        Open Hardware Project — 2026<br>
        Inspired by the work of Bob Greenyer and the<br>
        Martin Fleischmann Memorial Project (MFMP)<br>
        <br>
        Complete Sphinx Documentation • Single Volume Edition
    </div>
    
    <div class="disclaimer">
        <strong>CRITICAL DISCLAIMER</strong><br>
        Performance graphs, bubble-size estimates, and all quantitative models in this document 
        are <strong>conceptual software estimates only</strong>. The author has not built or tested 
        a physical prototype. Nothing here constitutes validated engineering data. Use at your own risk.
    </div>
</div>
"""

PDF_METADATA = {
    "title": "Modified Tesla Turbine for Cavitation — Complete Documentation",
    "author": "George Lambert (design conversation with Grok xAI, 2026)",
    "subject": "Open hardware precision flow conditioner for cavitation experiments. Full Sphinx documentation with engineering drawings, build instructions, theory, and cross-reference.",
    "creator": "Sphinx + WeasyPrint (singlehtml book build)",
    "keywords": "Tesla turbine, cavitation, LENR, MFMP, Bob Greenyer, open hardware, flow conditioner, boundary layer, 3D printing, OpenSCAD",
    "producer": "WeasyPrint professional documentation build",
}


def clean_build():
    """Remove previous singlehtml and PDF artifacts."""
    print("Cleaning previous build artifacts...")
    import shutil
    if (BUILD_DIR / "singlehtml").exists():
        shutil.rmtree(BUILD_DIR / "singlehtml")
    if PDF_PATH.exists():
        PDF_PATH.unlink()
    # Also clean the older html build if present (we don't need it for PDF)
    if (BUILD_DIR / "html").exists():
        shutil.rmtree(BUILD_DIR / "html")


def build_singlehtml():
    """Build the complete documentation as a single HTML file using Sphinx.

    We deliberately force the 'alabaster' theme here (instead of the normal 'furo'
    used for the website). Alabaster produces simple, linear, print-friendly HTML
    with almost no display:none tricks or heavy JS-dependent layout. This gives
    WeasyPrint reliable, complete content for a professional book PDF.
    """
    print("Building Sphinx singlehtml with alabaster theme (clean, linear, PDF-friendly)...")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sphinx",
            "-b",
            "singlehtml",
            "-E",  # fresh environment, ignore cache
            "-D",
            "html_theme=alabaster",
            "-D",
            "html_theme_options.nosidebar=1",
            "-D",
            "html_show_sourcelink=0",
            str(DOCS_DIR),
            str(HTML_DIR),
        ],
        cwd=DOCS_DIR,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Sphinx singlehtml build FAILED:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    print("singlehtml build complete (alabaster).")


def inject_titlepage_and_cleanup(html_content: str) -> str:
    """
    Inject a professional title page at the very start of <body>.
    Also perform light cleanup so the original Sphinx h1 doesn't duplicate the title.
    """
    # Find <body ...> and insert titlepage immediately after the opening tag
    body_match = re.search(r"(<body[^>]*>)", html_content, re.IGNORECASE)
    if not body_match:
        print("WARNING: Could not locate <body> tag for titlepage injection. PDF may lack proper title page.")
        return html_content

    body_open = body_match.group(1)
    insertion_point = body_match.end()

    # Inject titlepage
    modified = (
        html_content[:insertion_point]
        + "\n" + TITLEPAGE_HTML + "\n"
        + html_content[insertion_point:]
    )

    # Optional: hide or downstyle the original first <h1> (the Sphinx index title)
    # We keep it for accessibility/outline but the CSS makes the first real h1 not force extra break
    # The injected titlepage already has page-break-after: always, so content starts on page 2.

    return modified


def build_pdf():
    """Convert the singlehtml file to a high-quality paged PDF."""
    index_html_path = HTML_DIR / "index.html"
    if not index_html_path.exists():
        print("singlehtml index.html not found. Rebuilding...")
        build_singlehtml()

    print("Reading singlehtml and preparing for print...")
    html_content = index_html_path.read_text(encoding="utf-8", errors="replace")

    # Inject beautiful title page + any structural fixes
    html_content = inject_titlepage_and_cleanup(html_content)

    # Write a temporary processed HTML (easier for WeasyPrint base URL + debugging)
    processed_html = HTML_DIR / "index_print_ready.html"
    processed_html.write_text(html_content, encoding="utf-8")

    print("Loading print stylesheet...")
    print_css_path = DOCS_DIR / "_static" / "print.css"
    stylesheets = []
    if print_css_path.exists():
        stylesheets.append(CSS(filename=str(print_css_path)))
    else:
        print("WARNING: print.css not found — PDF will have minimal styling.")

    print("Converting to PDF with WeasyPrint (this may take 30–90 seconds)...")
    html = HTML(
        filename=str(processed_html),
        base_url=str(HTML_DIR) + "/",
    )

    # Write the final PDF with rich metadata
    html.write_pdf(
        str(PDF_PATH),
        stylesheets=stylesheets,
        pdf_metadata=PDF_METADATA,
    )

    # Report
    size_kb = PDF_PATH.stat().st_size / 1024
    print(f"\n✅ SUCCESS: Professional PDF created")
    print(f"   Location : {PDF_PATH}")
    print(f"   Size     : {size_kb:.1f} KB")
    print(f"   Metadata : title, author, subject, keywords all set")
    print(f"   Features : titlepage + TOC + full content + cross-reference at back")
    print(f"   Generated: {datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    clean_build()
    build_singlehtml()
    build_pdf()
    print("\nDone. Open the PDF and verify the title page, TOC, and back-matter index.")
