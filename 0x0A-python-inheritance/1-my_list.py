#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """function that   prints  lists in a sorted format"""
        print(sorted(self))
