#!/usr/bin/python3
"""This file appends and creates
 if file does not exist
"""


def append_write(filename="", text=""):
    """append to a file and create if it does not exist

    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return (f.write(text))
