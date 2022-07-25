#!/usr/bin/python3
"""
This file contains the definition of the
load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates a python object from a JSON file
    Args:
        filename (str): name of the file containing the json string
    """

    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
