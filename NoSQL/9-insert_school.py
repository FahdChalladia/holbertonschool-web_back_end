#!/usr/bin/env python3
"""
module for NoSQl (mongodb)
"""



def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
