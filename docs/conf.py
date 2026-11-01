# Sphinx configuration for the project hub (landing page).
# Replace every YOUR-ORG / tool-* placeholder.

project = "YOUR PROJECT NAME"
author = "Val"
copyright = "2026, Val"

extensions = [
    "myst_nb",                 # Markdown (.md) + Jupyter notebooks (.ipynb)
    "sphinx_design",           # cards, grids, tabs on the landing page
    "sphinx_copybutton",       # copy button on code blocks
    "sphinx.ext.intersphinx",  # link into each tool's own API docs
    "sphinx.ext.githubpages",
]

# Notebooks are rendered with their saved outputs, NOT re-executed in CI
# (no EM data or GPUs on GitHub runners). Run them locally before committing.
nb_execution_mode = "off"

myst_enable_extensions = ["colon_fence", "deflist"]

exclude_patterns = ["_build", "**.ipynb_checkpoints", "requirements.txt"]

# Cross-repo links. Uncomment once each tool repo publishes its own Sphinx docs;
# then e.g. {py:func}`tool_one.segment` in a tutorial links to that tool's API page.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    # "tool_one": ("https://YOUR-ORG.github.io/tool-one/", None),
    # "tool_two": ("https://YOUR-ORG.github.io/tool-two/", None),
}

html_theme = "pydata_sphinx_theme"
html_title = project
html_static_path = ["_static"]
html_theme_options = {
    "github_url": "https://github.com/YOUR-ORG",
    "navbar_align": "left",
    "show_toc_level": 2,
    "external_links": [
        {"name": "Paper", "url": "https://doi.org/YOUR-DOI"},
    ],
}
