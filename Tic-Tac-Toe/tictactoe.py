"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    x_num = o_num = 0
    for array in board:
        x_num += array.count("X")
        o_num += array.count("O")
    
    if x_num == o_num:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
            
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY or action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError 
    
    result = copy.deepcopy(board)
    if player(board) == "X":
        result[action[0]][action[1]] = "X"
    else:
        result[action[0]][action[1]] = "O"
    
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] != EMPTY:
            return board[i][0]
    
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[2][j] != EMPTY:
            return board[0][j]
    
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        if board[1][1] != EMPTY:
            return board[1][1]
                
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
                
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    
    if player == "X":
        return 1
    elif player == "O":
        return -1
    else:
        return 0
    
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == "X":
        maximum = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > maximum:
                maximum = value
                moves = [action]
            elif value == maximum:
                moves.append(action)
    else:
        minimum = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < minimum:
                minimum = value
                moves = [action]
            elif value == minimum:
                moves.append(action)  
    
    return random.choice(moves)


def min_value(state):
    """
    Returns the minimum value for all the possible actions.
    """
    value = math.inf
    
    if terminal(state):
        return utility(state)
    
    for action in actions(state):
        value = min(value, max_value(result(state, action)))
    
    return value


def max_value(state):
    """
    Returns the maximum value for all the possible actions.
    """
    value = -math.inf
    
    if terminal(state):
        return utility(state)
    
    for action in actions(state):
        value = max(value, min_value(result(state, action)))
    
    return value
