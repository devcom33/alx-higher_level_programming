#!/usr/bin/python3
"""adds all arguments to a Python list, and then save"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
c = load_from_json_file("add_item.json")
c.append(args)
save_to_json_file(c, "add_item.json")
