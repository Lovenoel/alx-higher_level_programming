#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared_rows = map(lambda row: list(map(lambda x: x ** 2, row)), matrix)
    squared_matrix = list(squared_rows)
    return squared_matrix
