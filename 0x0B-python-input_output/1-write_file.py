#!/usr/bin/python3
"""
function wrtie_file
"""


def write_file(filename="", text=""):
	"""return the number of ch written to filename from ..."""
	with open(filename, 'w', encoding='utf=8') as f:
		return f.write(text)
