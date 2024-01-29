#!/usr/bin/python3
"""A module of The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen at the specified position.

    Args:
    - board (list): The current board configuration.
    - row (int): The row to check for placing the queen.
    - col (int): The column to check for placing the queen.
    - n (int): The size of the chessboard.

    Returns:
    - bool: True if it is safe to place the queen; False otherwise.
    """
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """
    Print the solution in the required format.

    Args:
    - board (list): The current board configuration.
    """
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def solve_nqueens(board, row, n):
    """
    Solve the N Queens problem using backtracking.

    Args:
    - board (list): The current board configuration.
    - row (int): The current row being considered.
    - n (int): The size of the chessboard.
    """
    if row == n:
        # All queens are placed, print the solution
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen and move to the next row
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Main function to solve the N Queens problem.

    Args:
    - n (int): The size of the chessboard.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 values
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    # Command-line argument handling
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
