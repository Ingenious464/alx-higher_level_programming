#!/usr/bin/python3
"""Only a sub class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class; False otherwise"""
    return (type(obj) is not a_class 
