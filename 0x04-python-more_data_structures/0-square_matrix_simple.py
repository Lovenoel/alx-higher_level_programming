#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_matrix.append([num**2 for num in row])
    return squared_matrix
