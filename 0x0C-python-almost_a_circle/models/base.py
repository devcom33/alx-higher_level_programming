#!/usr/bin/python3
"""the first class Base"""


class Base:
	__nb_objects = 0
	def __init__(self, id=None):
		"""Construnctor init for assign id"""
		if id != None:
			self.id = id
		else:
			__nb_objects += 1
			self.id = __nb_objects
