#!/usr/bin/python3


def read_file(filename=""):
    """Reads a file and prints it to stdout

Args:
    filename (str): name of the file to be read
    """
    with open(filename, encoding="utf-8") as f:
        fc = f.read(2000)
        print(fc, end="")
