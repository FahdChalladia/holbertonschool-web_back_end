#!/usr/bin/env python3
"""
Simple helper function for pagination
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index
    for the given page and page_size in a list.

    Parameters:
        page (int): the current page number (1-indexed)
        page_size (int): the number of items per page

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
