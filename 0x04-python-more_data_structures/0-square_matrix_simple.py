#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    """compute square of all the int elements in the matric"""
    my_matrix = [[j**2 for j in row] for row in matrix]
    return my_matrix
