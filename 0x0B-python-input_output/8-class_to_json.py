#!/usr/bin/python3
"""Class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure list."""
    return obj.__dict__
