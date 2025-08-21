#!/usr/bin/env python3
"""
module for NoSQl (mongodb)
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document based on its name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

