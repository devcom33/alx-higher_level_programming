#!/usr/bin/python3
""" class Student that defines a studen"""


class Student:
    """constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieves a dictionary representation"""
    def to_json(self):
        return self.__dict__
