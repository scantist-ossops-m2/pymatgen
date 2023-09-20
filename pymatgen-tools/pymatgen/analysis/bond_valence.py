"""This module implements classes to perform bond valence analyses."""
from __future__ import annotations

import warnings

from pymatgen.core.bond_valence import *

warnings.warn(
    "pymatgen.analysis.bond_valence has been moved to pymatgen.core.bond_valence. This "
    "stub will be removed from v2025.1.1",
    DeprecationWarning,
)
