#!/usr/bin/python3
"""Class Is same"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class and False if its not"""
    if type(obj) is a_class:
        return True
    else:
        return False
