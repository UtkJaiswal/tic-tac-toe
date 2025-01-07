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

    
    def switch_player(self):
        self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O


    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):

                if self.board[row][col] == EMPTY:

                    self.board[row][col] = PLAYER_O
                    score = self.minimax(self.board, False)
                    self.board[row][col] = EMPTY

                    if score > best_score:

                        best_score = score
                        best_move = (row, col)
                        
        return best_move

    
    def minimax(self, board, is_maximizing):
        
        if self.check_win():

            if is_maximizing:
                return 1

            else:
                return 0

        if self.check_draw():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):

                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O

                        score = self.minimax(board, False)
                        board[row][col] = EMPTY

                        best_score = max(score, best_score)

            return best_score

        else:

            best_score = float('inf')

            for row in range(3):
                for col in range(3):

                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_X
                        score = self.minimax(board, True)
                        board[row][col] = EMPTY
                        best_score = min(score, best_score)

            return best_score


    def play_game(self):

        while not self.game_over:

            self.display_board()
            
            if self.mode == 'two-player' or self.current_player == PLAYER_X:

                print(f"Player {self.current_player}'s turn:")

                row, col = map(int, input("Enter row and column (0-2): ").split())

                if self.make_move(row, col):

                    if self.check_win():

                        self.display_board()
                        print(f"Player {self.current_player} wins!")
                        self.game_over = True

                    elif self.check_draw():

                        self.display_board()
                        print("It's a draw!")
                        self.game_over = True

                    else:

                        self.switch_player()

                else:

                    print("Invalid move. Try again.")

            else:

                print(f"Player {self.current_player}'s turn (AI):")
                row, col = self.ai_move()
                self.make_move(row, col)

                if self.check_win():

                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    self.game_over = True

                elif self.check_draw():

                    self.display_board()
                    print("It's a draw!")
                    self.game_over = True

                else:

                    self.switch_player()
    

def choose_mode():
    mode = input("Choose game mode (two-player/single-player): ").strip().lower()
    if mode not in ['two-player', 'single-player']:
        print("Invalid mode. Defaulting to two-player mode.")
        return 'two-player'
    return mode
    