# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Q1K_neuroimaging"
copyright = "2023, Scott Huberty, Diksha Srishyla, Gabriel Blanco Gomez"
author = "Scott Huberty, Diksha Srishyla, Gabriel Blanco Gomez"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx design adds grid directive and other responsive components
# Sphinxemoji So we can use emoji's in docs.
# contrib extensions youtube for embedding youtube videos
extensions = [
    "sphinx_design",
    "sphinxemoji.sphinxemoji",
    # contrib extensions
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
# html_static_path = ["_static"]

# Enable numref for automatically numbering Figures, i.e "Fig 1"
numfig = True
