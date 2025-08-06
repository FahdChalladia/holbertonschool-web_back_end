#!/usr/bin/env python3
"""Module that converts a key and value to a tuple with squared value."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and the square of the int/float value."""
    return (k, float(v ** 2))
