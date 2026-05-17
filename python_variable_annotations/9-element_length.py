#!/usr/bin/env python3
"""Module"""

from typing import List, Tuple, Iterable


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """Function"""

    return [(i, len(i)) for i in lst]