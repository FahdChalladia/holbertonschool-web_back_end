#!/usr/bin/env python3
"""
module for basic pagination
"""


def index_range(page, page_size):
    """function that return start and end index"""
    return {(page_size*(page-1)), page_size*page}
