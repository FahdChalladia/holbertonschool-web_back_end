#!/usr/bin/env python3
"""Module containing an async generator that yields random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that loops 10 times, each iteration
    waits 1 second asynchronously and yields a random float
    between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
