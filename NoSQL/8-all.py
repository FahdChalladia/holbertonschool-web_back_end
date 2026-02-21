#!/usr/bin/env python3
"""8-all.py"""
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of documents. Empty list if none found.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
