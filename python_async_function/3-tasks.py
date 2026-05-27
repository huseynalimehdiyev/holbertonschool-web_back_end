#!/usr/bin/env python3
"""Module"""

import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function"""

    return asyncio.create_task(wait_random(max_delay))
