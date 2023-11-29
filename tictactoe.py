import csv
import os

# Define the path for the log file
LOG_FILE_PATH = 'logs/game_log.csv'

def record_winner(winner):
    with open(LOG_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['Winner']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(LOG_FILE_PATH) == 0:
            writer.writeheader()

        writer.writerow({'Winner': winner})

def record_game_statistics(player1, player2, winner, moves):
    with open(LOG_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['Player1', 'Player2', 'Winner', 'TotalMoves']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(LOG_FILE_PATH) == 0:
            writer.writeheader()

        writer.writerow({'Player1': player1, 'Player2': player2, 'Winner': winner, 'TotalMoves': moves})

# Update your TicTacToeGame class to include player names
class TicTacToeGame:
    def __init__(self, player1, player2, player1_name="Player 1", player2_name="Player 2"):
        self.board = make_empty_board()
        self.current_player = 'X'
        self.player1 = player1
        self.player2 = player2
        self.player1_name = player1_name
        self.player2_name = player2_name

    def play_game(self):
        total_moves = 0
        while True:
            print_board(self.board)
            print(f"{self.player1_name}: X, {self.player2_name}: O")

            try:
                if self.current_player == 'X':
                    row, col = self.player1.make_move(self.board)
                else:
                    row, col = self.player2.make_move(self.board)

                if row not in (0, 1, 2) or col not in (0, 1, 2):
                    raise ValueError("Invalid input. Row and column must be 0, 1, or 2.")

                if move_step(self.board, row, col, self.current_player):
                    winner = get_winner(self.board)
                    total_moves += 1

                    if winner:
                        print_board(self.board)
                        print(f"{self.player1_name if winner == 'X' else self.player2_name} wins!")
                        record_winner(self.player1_name if winner == 'X' else self.player2_name)
                        record_game_statistics(self.player1_name, self.player2_name, winner, total_moves)
                        break
                    elif is_full(self.board):
                        print_board(self.board)
                        print("It's a draw!")
                        record_game_statistics(self.player1_name, self.player2_name, 'Draw', total_moves)
                        break

                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                else:
                    print("Position is taken, try again.")
            except ValueError as e:
                print(str(e))

# The rest of your code remains the same
