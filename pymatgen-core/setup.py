"""Pymatgen package configuration."""

from __future__ import annotations

import platform
import sys

import numpy as np
from setuptools import Extension, find_namespace_packages, setup

is_win_64 = sys.platform.startswith("win") and platform.machine().endswith("64")
extra_link_args = ["-Wl,--allow-multiple-definition"] if is_win_64 else []

with open("README.md") as file:
    long_description = file.read()

# unlike GitHub readme's, PyPI doesn't support <picture> tags used for responsive images
# (i.e. adaptive to OS light/dark mode)
# NOTE this manual fix won't work once we migrate to pyproject.toml
logo_url = "https://raw.githubusercontent.com/materialsproject/pymatgen/master/docs/_images/pymatgen.svg"
long_description = (
    f"<h1 align='center'><img alt='Logo' src='{logo_url}' height='70'></h1>" + long_description.split("</picture>")[-1]
)

setup(
    name="pymatgen_core",
    packages=find_namespace_packages(
        include=["pymatgen.*"],
    ),
    version="2023.9.10",
    python_requires=">=3.9",
    install_requires=[
        "matplotlib>=1.5",
        "monty>=3.0.2",
        "numpy>=1.20.1",
        "palettable>=3.1.1",
        "requests",
        "ruamel.yaml>=0.17.0",
        "scipy>=1.5.0",
        "spglib>=2.0.2",
        "tabulate",
        "tqdm",
        "networkx",
    ],
    extras_require={
        "dev": [
            "black",
            "mypy",
            "pre-commit",
            "pytest-cov",
            "pytest-split",
            "pytest",
            "ruff",
        ],
        "docs": [
            "sphinx",
            "sphinx_rtd_theme",
            "doc2dash",
        ],
    },
    # All package data has to be explicitly defined. Do not use automated codes like last time. It adds
    # all sorts of useless files like test files and is prone to path errors.
    package_data={
        "pymatgen.core": ["*.json"],
        "pymatgen": ["py.typed"],
        "pymatgen.util": ["structures/*.json", "*.json"],
        "pymatgen.symmetry": ["*.yaml", "*.json", "*.sqlite"],
    },
    author="Pymatgen Development Team",
    author_email="ongsp@ucsd.edu",
    maintainer="Shyue Ping Ong, Matthew Horton, Janosh Riebesell",
    maintainer_email="ongsp@ucsd.edu, mkhorton@lbl.gov, janosh.riebesell@gmail.com",
    url="https://pymatgen.org",
    license="MIT",
    project_urls={
        "Docs": "https://pymatgen.org",
        "Package": "https://pypi.org/project/pymatgen",
        "Repo": "https://github.com/materialsproject/pymatgen",
    },
    description="Python Materials Genomics is a robust materials "
    "analysis code that defines core object representations for "
    "structures and molecules with support for many electronic "
    "structure codes. It is currently the core analysis code "
    "powering the Materials Project "
    "(https://materialsproject.org).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "ABINIT",
        "analysis",
        "crystal",
        "diagrams",
        "electronic",
        "gaussian",
        "materials",
        "nwchem",
        "phase",
        "project",
        "qchem",
        "science",
        "structure",
        "VASP",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    ext_modules=[
        Extension(
            "pymatgen.optimization.linear_assignment",
            ["pymatgen/optimization/linear_assignment.pyx"],
            extra_link_args=extra_link_args,
        ),
        Extension("pymatgen.util.coord_cython", ["pymatgen/util/coord_cython.pyx"], extra_link_args=extra_link_args),
        Extension(
            "pymatgen.optimization.neighbors",
            ["pymatgen/optimization/neighbors.pyx"],
            extra_link_args=extra_link_args,
        ),
    ],
    include_dirs=[np.get_include()],
)
