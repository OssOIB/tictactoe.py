import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the boardss.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    


def min_value(board):
    

def print_board(board):
    """
    Prints the current state of the board.
    """
    
def play():
    """
    Plays a game of tic-tac-toe.
    """
   