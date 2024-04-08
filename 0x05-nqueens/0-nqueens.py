#!/usr/bin/python3
"""Solve nqueens problem"""
import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False

    return True


def solve_n_queens(n, board, row=0, solutions=[]):
    """Solve n queens problem"""
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1, solutions)


def print_solutions(solutions):
    """helper function to print board"""
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])


def main():
    """solve nqueens problem"""
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

    board = [-1] * N
    solutions = []
    solve_n_queens(N, board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    """Init and checks"""
    main()
