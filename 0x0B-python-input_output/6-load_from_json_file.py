#!/usr/bin/python3
"""a function that writes an Object to a text file"""
import json


def load_from_json_file(filename):
    """ loadfrom_json_file: create an Object from json file
        Args:
            filename: file
        Returns: String
    """
    with open(filename):
        return json.loads(filename)
