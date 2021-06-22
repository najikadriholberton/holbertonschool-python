#!/usr/bin/python3
"""List MongoDB collection documents"""
import pymongo


def list_all(mongo_collection):
    """list documents within collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
