#!/usr/bin/env python3
"""Module"""

from typing import List, Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Function"""

    if lst:
        return lst[0]
    else:
        return None
