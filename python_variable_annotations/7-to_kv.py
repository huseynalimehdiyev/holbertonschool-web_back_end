#!/usr/bin/env python3
"""Module"""

from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Function"""

    return (k, float(v ** 2))
