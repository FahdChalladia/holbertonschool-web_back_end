#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> dict:
    """Return dataset with next_index that works even after deletions"""
    dataset = self.indexed_dataset()
    assert isinstance(index, int) and 0 <= index < len(dataset), "index out of range"
    assert isinstance(page_size, int) and page_size > 0, "page_size must be positive"

    data = []
    current_index = index
    collected = 0
    keys = sorted(dataset.keys())
    while collected < page_size and current_index <= keys[-1]:
        if current_index in dataset:
            data.append(dataset[current_index])
            collected += 1
        current_index += 1

    next_index = current_index if current_index <= keys[-1] else None

    return {
        "index": index,
        "next_index": next_index,
        "page_size": len(data),
        "data": data
    }
