PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    
    def __init__(self, mode='two-player'):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.current_player = PLAYER_X
        self.game_over = False
        self.mode = mode


    def display_board(self):
        print("\n")
        for row in self.board:
            print(" | ".join(row))
            print("---------")

        print("\n")


    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == EMPTY:
            return True
        return False

