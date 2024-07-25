#!/usr/bin/python3
""" method that determines"""


def validUTF8(data):
    """ method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    try:
        data.decode('UTF-8')
        return True
    except UnicodeDecodeError:
        False
