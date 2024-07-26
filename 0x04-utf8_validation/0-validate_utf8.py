#!/usr/bin/python3
""" method that determines"""


def validUTF8(data):
    """ method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    if not all(0 <= byte <= 255 for byte in data):
        return False
    try:
        datas = bytes(data)
        datas.decode('UTF-8')
        return True
    except (UnicodeDecodeError, TypeError):
        False
