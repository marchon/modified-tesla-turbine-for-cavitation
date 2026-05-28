# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../python'))

project = 'Modified Tesla Turbine for Cavitation'
copyright = '2026, Marchon & contributors (MFMP open hardware spirit)'
author = 'Marchon (design conversation with Grok xAI, May 2026)'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'myst_parser',           # Markdown support
    'sphinxcontrib.plantuml', # diagrams (if plantuml installed)
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'          # clean modern theme; falls back gracefully
html_static_path = ['_static']
html_title = "Modified Tesla Turbine for Cavitation — Complete Documentation"
html_short_title = "Tesla Turbine Cavitation Docs"

# Single-page HTML (used by the professional PDF builder)
# and general HTML settings
html_use_index = True
html_domain_indices = True
html_show_sourcelink = False

# Include print stylesheet for PDF generation via WeasyPrint
html_css_files = ['print.css']

# Math
mathjax3_config = {
    'tex': {'packages': {'[+]': ['physics']}}
}

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# PlantUML (optional)
plantuml = 'plantuml'
plantuml_output_format = 'svg'

# =============================================================================
# LaTeX / PDF Output — Robust & Professional Configuration
#
# NOTE: The primary high-quality "entire Sphinx docs in one PDF" path is
#       docs/build_pdf.py (singlehtml + WeasyPrint + custom book CSS).
#       It produces the titlepage + TOC + cross-reference the user requested.
#
#       The native Sphinx LaTeX builder below requires a full TeX Live install
#       (wrapfig, etc.). It is kept as a secondary option.
# =============================================================================

# Use pdflatex for maximum compatibility across TeX installations
latex_engine = 'pdflatex'

# Define a clean manual-style document
latex_documents = [
    (
        'index',
        'modifiedteslaturbineforcavitation.tex',
        'Modified Tesla Turbine for Cavitation',
        'George Lambert',
        'manual',
        True,
    ),
]

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',

    # Use standard, widely available fonts
    'preamble': r'''
    \usepackage[T1]{fontenc}
    \usepackage{lmodern}
    \usepackage{helvet}
    \renewcommand{\familydefault}{\sfdefault}

    % Good code formatting
    \usepackage{listings}
    \lstset{
        basicstyle=\ttfamily\small,
        breaklines=true,
        frame=single,
        backgroundcolor=\color{gray!10},
    }

    % Clean hyperlinks
    \hypersetup{
        colorlinks=true,
        linkcolor=blue!70!black,
        urlcolor=blue!80!black,
    }
    ''',

    # Disable fancy chapter package that often causes missing file errors
    'fncychap': '',

    'extraclassoptions': 'openany,oneside',

    # Reasonable margins
    'sphinxsetup': 'hmargin=0.9in,vmargin=0.85in',

    # Custom title page
    'maketitle': r'''
    \begin{titlepage}
    \centering
    \vspace*{1.8cm}
    {\Huge\bfseries Modified Tesla Turbine\\[0.35cm] for Cavitation\par}
    \vspace{0.9cm}
    {\Large Precision Flow Conditioner\\[0.2cm] for Reproducible Cavitation Experiments\par}
    \vspace{1.6cm}
    {\large George Lambert\par}
    \vspace{0.25cm}
    {Litchfield, New Hampshire \quad | \quad 2026\par}
    \vfill
    {\small Open Hardware Project — Inspired by Bob Greenyer and the MFMP\par}
    \end{titlepage}
    ''',

    # Table of contents
    'tableofcontents': r'\tableofcontents',

    # Index at the back
    'printindex': r'\printindex',
}
