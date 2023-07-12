#!/usr/bin/python3
"""
read_file func
"""

def read_file(filename=""):
    """read a txt (UTD-8) and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
