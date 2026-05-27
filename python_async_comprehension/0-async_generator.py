#!/usr/bin/env python3
"""Module"""

import asyncio
import random


async def async_generator() -> asyncio.Generator[float, None, None]:
    """Function"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.unfirm(0, 10)

