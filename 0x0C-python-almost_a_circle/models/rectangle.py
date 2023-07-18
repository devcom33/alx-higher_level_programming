#!/usr/bin/python3
""" a rectangle model"""

from models.base import Base


class Rectangle(Base):
	""" A rectangle """

	def __init__(self, width, height, x=0, y=0, id=None):
		"""Initialize a new Rectangle.

        	Args:
			width (int): The width of the Rec.
            		height (int): The height of the Rec.
			x (int): The x of the Rec.
			y (int): The y of the Rec.
			id (int): The id of the new Rec.
        	"""
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		super().__init__(id)
	@property
	def width(self):
		"""get of the width"""
		return self.__width

	@width.setter
	def width(self, value):
		""" setter of the width """
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value
	@property
	def height(self):
		"""get the height"""
        	return self.__height

	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value
