#!/usr/bin/python3
"""This module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
