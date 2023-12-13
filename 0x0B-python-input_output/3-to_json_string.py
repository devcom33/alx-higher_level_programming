#!/usr/bin/python3
"""a function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
        Args:
            my_obj: an object
        Returns:
            String of object
    """
    return json.dumps(my_obj)
