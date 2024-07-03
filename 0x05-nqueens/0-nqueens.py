#!/usr/bin/python3
"""N queens"""
import sys


def is_safe(board, row, col):
    """Check if there's a queen in the same row to the left"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """If all queens are placed, add the solution"""
    if col >= len(board):
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0
    return res


def solve_nqueens(n):
    """Initialize the board with all zeros"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


if __name__ == "__main__":
    """Check if the number of arguments is correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
