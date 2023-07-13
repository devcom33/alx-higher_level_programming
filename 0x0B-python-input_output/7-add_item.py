#!/usr/bin/python3
"""adds all arguments to a Python list, and then save"""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """adds all arguments to a Python list"""
    args = sys.argv[1:]
    c = load_from_json_file("add_item.json")
    c.append(args)
    save_to_json_file(c, "add_item.json")

