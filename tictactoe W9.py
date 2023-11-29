
class TicTacToeGame:
    
    def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(" ".join([str(cell) if cell is not None else ' ' for cell in row]))

def move_step(board, row, col, player):
    if board[row][col] is None:
        board[row][col] = player
        return True
    else:
        return False

def get_winner(board):
    # Implement logic to check for a winner
    pass

def is_full(board):
    for row in board:
        if None in row:
            return False
    return True

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = make_empty_board()
        self.current_player = 'X'
        self.player1 = player1
        self.player2 = player2

    def play_game(self):
        while True:
            print_board(self.board)
            print(f"Player {self.current_player}'s turn")

            try:
                if self.current_player == 'X':
                    row, col = self.player1.make_move(self.board)
                else:
                    row, col = self.player2.make_move(self.board)

                if row not in (0, 1, 2) or col not in (0, 1, 2):
                    raise ValueError("Invalid input. Row and column must be 0, 1, or 2.")

                if move_step(self.board, row, col, self.current_player):
                    winner = get_winner(self.board)
                    if winner:
                        print_board(self.board)
                        print(f"Player {winner} wins!")
                        break
                    elif is_full(self.board):
                        print_board(self.board)
                        print("It's a draw!")
                        break
                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                else:
                    print("Position is taken, you should try it again.")
            except ValueError as e:
                print(str(e))

class HumanPlayer:
    def make_move(self, board):
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number.")

class BotPlayer:
    def make_move(self, board):
        import random
        return random.randint(0, 2), random.randint(0, 2)


    def record_winner(self, winner):
        with open("game_log.csv", "a") as log_file:
            log_file.write(f"{winner}\n")

# 在 play_game 方法中，调用 record_winner 方法记录获胜者
# 在  winner = get_winner(self.board) 之后添加
self.record_winner(winner)
