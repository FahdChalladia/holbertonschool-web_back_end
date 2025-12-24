#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Return the dataset with deletion-resilient hypermedia pagination.

        Args:
            index (int): start index of the page.
            page_size (int): number of items to return.

        Returns:
            Dict: dictionary containing index, next_index, page_size, and data.
        """
        assert isinstance(index, int) \
            and 0 <= index < len(self.indexed_dataset())

        dataset = self.indexed_dataset()
        data = []
        next_index = index
        count = 0

        while count < page_size and next_index < len(dataset):
            if next_index in dataset:
                data.append(dataset[next_index])
                count += 1
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
