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
copyright = '2022, glitter'
author = 'glitter'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
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

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'show-inheritance': None,
}
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'glitter_sdk'
now = datetime.datetime.now()
copyright = str(now.year) + ', BigchainDB Contributors'
version = glitter_sdk.__version__
release = glitter_sdk.__version__
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True
suppress_warnings = ['image.nonlocal_uri']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'bigchaindb_python_driverdoc'

latex_elements = {}

latex_documents = [
    ('index', 'bigchaindb_python_driver.tex',
     'BigchainDB Python Driver Documentation',
     'BigchainDB', 'manual'),
]

man_pages = [
    ('index', 'bigchaindb_python_driver',
     'BigchainDB Python Driver Documentation',
     ['BigchainDB'], 1)
]

texinfo_documents = [
    ('index', 'bigchaindb_python_driver',
     'BigchainDB Python Driver Documentation',
     'BigchainDB',
     'bigchaindb_python_driver',
     '',
     'Miscellaneous'),
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'bigchaindb-server': (
        'https://docs.bigchaindb.com/projects/server/en/latest/', None),
}
