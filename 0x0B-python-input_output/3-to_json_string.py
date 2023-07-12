#!/usr/bin/python3
"""the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """return the JSON representation"""
    return json.dumps(my_obj)
