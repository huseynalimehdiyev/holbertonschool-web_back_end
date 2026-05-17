#!/usr/bin/env python3
"""Module"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function"""

    return (k, float(v ** 2))
