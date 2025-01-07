PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self, mode='two-player'):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.current_player = PLAYER_X
        self.game_over = False
        self.mode = mode