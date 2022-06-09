#!/usr/bin/python3
# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """multiply a dictionary by 2 and return"""
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
