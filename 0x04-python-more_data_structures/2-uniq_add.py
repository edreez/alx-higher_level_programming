#!/usr/bin/python3
# 2-uniq_add.py
def uniq_add(my_list=[]):
    """adding unique numbeers together only once for each number"""
    sum = 0
    for k in set(my_list):
        sum += k
    return (sum)
