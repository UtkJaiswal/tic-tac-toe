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



    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True

        return False


    def check_win(self):
        for i in range(3):

            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return True
        
        return False

        
    def check_draw(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True


    def check_draw(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True
    