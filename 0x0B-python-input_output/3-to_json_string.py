#!/usr/bin/python3
"""
This file dscries the to_json_string function
"""
import json


def to_json_string(my_obj):
    """Returns the JSON description of an object

    Args:
        my_obj (known): object to be converted to JSON format
    """

    return json.dumps(my_obj)
