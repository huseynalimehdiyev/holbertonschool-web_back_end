#!/usr/bin/env python3
"""
This module provides a function that safely gets a value from a dictionary.
"""

from typing import TypeVar, Mapping, Optional


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(
    dct: Mapping[K, V],
    key: K,
    default: Optional[V] = None
) -> Optional[V]:
    """Function"""
    if key in dct:
        return dct[key]
    else:
        return default