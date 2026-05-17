#!/usr/bin/env python3
"""Module"""

from typing import Callable


def make_multiplier(multiplier: float,) -> Callable[[float], float]:
    """Function"""

    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
