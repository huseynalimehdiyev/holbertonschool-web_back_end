#!/usr/bin/env python3
"""
This module provides a function that safely gets a value from a dictionary.
"""

from typing import TypeVar, Mapping, Optional, Any


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Any | T:
    """Function"""

    if key in dct:
        return dct[key]
    else:
        return default
