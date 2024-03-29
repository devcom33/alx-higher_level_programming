#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file
        Args:
            filename: name of the file
            text: content of the file
        Returns:
            the number of char
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
