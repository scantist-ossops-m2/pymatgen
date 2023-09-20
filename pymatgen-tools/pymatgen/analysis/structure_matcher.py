"""This module provides classes to perform fitting of structures."""

from __future__ import annotations

import warnings

from pymatgen.core.structure_matcher import *

warnings.warn(
    "pymatgen.analysis.structure_matcher has been moved to pymatgen.core.structure_matcher. This "
    "stub will be removed from v2025.1.1",
    DeprecationWarning,
)
