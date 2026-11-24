"""Configuration de Sphinx."""

import tomllib
from importlib.metadata import version as get_version
from pathlib import Path

with (Path(__file__).parent.parent / "pyproject.toml").open("rb") as f:
    data = tomllib.load(f)

project = data["project"]["name"]
author = ", ".join(a["name"] for a in data["project"]["authors"])
copyright = f"2026, {author}"  # noqa: A001
release = get_version(project)
version = release

extensions = [
    "sphinx.ext.autodoc",   # génère la doc à partir des docstrings
    "sphinx.ext.napoleon",  # comprend les docstrings au format numpy
]
napoleon_numpy_docstring = True
napoleon_google_docstring = False

language = "fr"
html_theme = "sphinx_rtd_theme"