#!/usr/bin/python3

"""the first class Base"""


class Base:
	"""Base Class

	this represents the Base Class

	__nb_objects: Num of inst
	"""

	__nb_objects = 0

	def __init__(self, id=None):
		"""Construnctor init for assign id

		Args;
			id : the id of the base
		"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
