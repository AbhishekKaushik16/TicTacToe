"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    zero = 0
    cross = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                cross += 1
            elif board[i][j] == "O":
                zero += 1
    if zero == (cross + 1):
        return "X"
    else:
        return "O"
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.append((i,j))
    return action
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return false
    return true
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
