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
html_title = "HDD Platter Flow Conditioner — Documentation"

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
