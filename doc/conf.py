# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import word2anki
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'word2anki'
copyright = '2024, Wizard-one'
author = 'Wizard-one'
release = word2anki.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
	'sphinx.ext.viewcode',  # Add a link to the Python source code for classes, functions etc.
	'numpydoc',# numpy style docstring parser
	'myst_parser'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
# html_theme_options = {}
html_theme_options = {
  # Navbar
  "github_url": "https://github.com/Wizard-one/word2anki",
  "navbar_end": ["navbar-icon-links"],
  # General config
  "collapse_navigation": True,
}