#!/usr/bin/python3
"""A module that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of lists: A new matrix where each element is the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row of the matrix doesn't have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists and each row has the same size
    if not isinstance(matrix, list) or not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the matrix division and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
