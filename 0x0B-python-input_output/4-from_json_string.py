#!/usr/bin/python3
"""from_json_string function documentation"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON strin"""
    return json.loads(my_str)
