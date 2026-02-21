#!/usr/bin/env python3
"""12-log_stats.py"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    query = {
        "method": "GET",
        "path": "/status"
    }
    status_count = collection.count_documents(query)
    print("{} status check".format(status_count))
