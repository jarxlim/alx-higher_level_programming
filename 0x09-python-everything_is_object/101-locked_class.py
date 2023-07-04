#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass:
    """
    only allows new instance attributes 'first_name
    """

    __slots__ = ["first_name"]
