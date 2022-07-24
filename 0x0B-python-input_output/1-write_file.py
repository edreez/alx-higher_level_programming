#!/bin/bash/python3
"""This file write and prints to stdout
"""


def write_file(filename="", text=""):
    """write to a file and return it to stdout

    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
