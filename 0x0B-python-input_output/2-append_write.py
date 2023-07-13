#!/usr/bin/python3
"""append_write function documentation"""


def append_write(filename="", text=""):
    """function appends a string at the end of a text file"""
    with open(filename, "a", encoding='utf-8') as myFile:
        return myFile.write(text)
