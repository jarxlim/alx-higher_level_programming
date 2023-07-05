#!/usr/bin/python3
''' solves the N queens problem.'''

import sys


def init_chessboard(c):
    """Initialize `n`x`n` sized chessboard"""
    board = []
    [board.append([]) for i in range(c)]
    [row.append(' ') for i in range(c) for row in board]
    return (board)


def board_copy(board):
    """Return a deepcopy."""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def solutions_getter(board):
    """list of lists representation of a solved chessboard."""
    soln = []
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == "Q":
                soln.append([a, b])
                break
    return (soln)


def x_out(board, row, col):
    """X out spots on a chessboard."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursion_soln(board, row, queens, solutions):
    """Recursion solution of N-queen problem."""

    if queens == len(board):
        solutions.append(solutions_getter(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_b = board_copy(board)
            tmp_b[row][c] = "Q"
            x_out(tmp_b, row, c)
            solutions = recursion_soln(tmp_b, row + 1, queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_chessboard(int(sys.argv[1]))
    solutions = recursion_soln(board, 0, 0, [])
    for solut in solutions:
        print(solut)
