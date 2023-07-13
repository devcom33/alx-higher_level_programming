#!/usr/bin/python3
"""a function that returns the dictionary description with simple ds"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
