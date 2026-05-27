#!/usr/bin/env python3
"""Module"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Function"""

    for _ in range(9):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
