#!/usr/bin/python3
"""Defines a Locked_Class"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes, except first_name
    """

    _slots_ = ["first_name"]
