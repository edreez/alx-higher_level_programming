#!/usr/bin/python3
"""
contains the definition of the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object an Object to a text file,
    using a JSON representation
    Args:
        my_obj (unknown): object to be written to file in JSON format
        filename (str): name of the file to write into
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
