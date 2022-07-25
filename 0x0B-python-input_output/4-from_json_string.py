#!/usr/bin/python3
"""
This file contains the definition of
 the from_json_string function
"""
import json


def from_json_string(my_str):
    """Returns the python data structure represented by a JSON string

    Args:
        my_str (JSON string): json string to be converted to python object
    """

    return json.loads(my_str)
