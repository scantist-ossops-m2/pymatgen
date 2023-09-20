"""This module defines convenience types for type hinting purposes.
Type hinting is new to pymatgen, so this module is subject to
change until best practices are established.
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

from pymatgen.core.composition import Composition
from pymatgen.core.periodic_table import DummySpecies, Element, Species

PathLike = Union[str, Path]

# Things that can be cast to a Species-like object using get_el_sp
SpeciesLike = Union[str, Element, Species, DummySpecies]

# Things that can be cast to a Composition
CompositionLike = Union[str, Element, Species, DummySpecies, dict, Composition]
