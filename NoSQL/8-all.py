#!/usr/bin/env python3
""" 9-insert_school """


def list_all(mongo_collection):
    """ 9-insert_school """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
