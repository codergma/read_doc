# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
import sphinx_rtd_theme

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.insert(0, project_root)
# sys.path.insert(0, os.path.dirname('../../glitter_sdk'))
# print(project_root)

import glitter_sdk

# -- Project information -----------------------------------------------------

project = 'glitter_sdk'
author = 'glitter'
now = datetime.datetime.now()
copyright = str(now.year) + ', glitter'
version = glitter_sdk.__version__
release = glitter_sdk.__release__

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
]
# -- Options for HTML output ----------------------------------------------
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'show-inheritance': None,
}
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True
suppress_warnings = ['image.nonlocal_uri']

htmlhelp_basename = 'glitter_python_driverdoc'

latex_elements = {}

# -- Options for LaTeX output ---------------------------------------------
latex_documents = [
    ('index', 'glitter_python_driver.tex',
     'Glitter Python Driver Documentation',
     'ted@glitterprotocol.io', 'manual'),
]

# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'glitter_python_driver',
     'Glitter Python Driver Documentation',
     ['ted@glitterprotocol.io'], 1)
]

# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    ('index', 'glitter_python_driver',
     'Glitter Python Driver Documentation',
     'ted@glitterprotocol.io',
     'glitter_python_driver',
     '',
     'Miscellaneous'),
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'Glitter-server': (
        'https://docs.Glitter.com/projects/server/en/latest/', None),
}
