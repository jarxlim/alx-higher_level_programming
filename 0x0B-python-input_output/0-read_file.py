#!/usr/bin/python3
"""read_file function doc"""


def read_file(filename=""):
    """a function that reads a text file then prints it to stdout"""

    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
