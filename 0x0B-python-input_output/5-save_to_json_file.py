#!/usr/bin/python3
"""a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file: writes an Object to a text file
        Args:
            my_obj: object
            filename: name of the file
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
