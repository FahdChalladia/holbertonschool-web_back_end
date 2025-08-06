#!/usr/bin/env python3
"""running multi coroutines concurrently and return ordered delays."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return a list of all the delays in ascending order.
    """
    delays = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    result = []
    for delay in delays:
        inserted = False
        for i in range(len(result)):
            if delay < result[i]:
                result.insert(i, delay)
                inserted = True
                break
        if not inserted:
            result.append(delay)
    return result
