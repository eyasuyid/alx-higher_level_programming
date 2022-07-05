#!/usr/bin/python3
"""student class"""


class Student:
    """define student
    attr:
        - firstname
        - lastname
        - age
    """
    def __init__(self, firstname, lastname, age):
        """Initializes the class with the given arguments"""

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self):
        """Return the description"""
        return self.__dict__
