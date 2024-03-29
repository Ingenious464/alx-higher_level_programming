#!/usr/bin/python3
"""From JSON string to-object"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) object represented by  a JSON string"""
    return json.loads(my_str)
