#!/usr/bin/python3
    """Write a string to a text file.(UTF8)"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.write(text)
