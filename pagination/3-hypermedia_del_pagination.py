#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
Provides a Server class that supports hypermedia pagination
resilient to deletions in the dataset.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a dataset of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with cached dataset and indexed dataset."""
        self.__dataset: List[List] = None
        self.__indexed_dataset: Dict[int, List] = None

    def dataset(self) -> List[List]:
        """Return cached dataset, loading it if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient hypermedia page starting at `index`.

        Args:
            index (int): starting index of page (default 0)
            page_size (int): number of items to return (default 10)

        Returns:
            Dict with keys:
                - index: current start index
                - next_index: next index to query for following page
                - page_size: actual number of items returned
                - data: list of items in current page
        """
        indexed_data = self.indexed_dataset()
        dataset_length = len(indexed_data)

        assert isinstance(index, int) and 0 <= index < dataset_length, \
            "Index out of range"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be positive"

        data: List[List] = []
        next_index = index
        collected = 0

        # Collect `page_size` items while skipping deleted entries
        while collected < page_size and next_index < dataset_length:
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                collected += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
