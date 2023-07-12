#!/usr/bin/python3
""" a function that creates an Object from a JSON"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
