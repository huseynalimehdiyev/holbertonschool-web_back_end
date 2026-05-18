#!/usr/bin/env python3
"""Module"""

from typing import Union, TypeVar, Mapping, Optional, Any


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """Function"""

    if key in dct:
        return dct[key]
    else:
        return default
