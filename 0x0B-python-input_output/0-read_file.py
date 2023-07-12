#!/usr/bin/python3
"""
read_file func
"""
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8"):
        print(f.read(), end="")
