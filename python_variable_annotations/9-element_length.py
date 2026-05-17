#!/usr/bin/env python3
"""Module"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function"""

    return [(i, len(i)) for i in lst]
