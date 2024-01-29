#!/usr/bin/python3
"""a module that defines a  class rectangle"""
import sys


def is_safe(board, row, col, n):
    # Check if a queen can be placed in this cell
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]

    def solve(board, col):
        if col >= n:
            for row in board:
                print("".join(['Q' if cell == 1 else '.' for cell in row]))
            print()
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
