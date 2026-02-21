#!/usr/bin/env python3
"""11-schools_by_topic.py"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents containing the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
