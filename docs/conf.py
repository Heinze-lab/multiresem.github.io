# Sphinx configuration for the project hub (landing page).
# Replace every YOUR-ORG / tool-* placeholder.

project = "vem-toolkit"
author = "Valentin Gillet"
copyright = "2026, Valentin Gillet"

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
    "emalign": ("https://github.com/Heinze-lab/EMalign", None),
    "emtrain": ("https://github.com/Heinze-lab/EMtrain", None),
    "emsegment": ("https://github.com/Heinze-lab/EMsegment", None),
    "synpred": ("https://github.com/Heinze-lab/SynPred", None),
    "lsdtopcg": ("https://github.com/Heinze-lab/LSDtoPCG", None)
}

html_theme = "pydata_sphinx_theme"
html_title = project
html_static_path = ["_static"]
html_theme_options = {
    "github_url": "https://github.com/Heinze-lab",
    "navbar_align": "left",
    "show_toc_level": 2,
    "external_links": [
        {"name": "Paper", "url": "https://doi.org/10.7554/eLife.110789.1"},
    ],
}
