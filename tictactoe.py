import csv
import os
import datetime  # For recording the timestamp

# Define the path for the log file
LOG_FILE_PATH = 'logs/game_log.csv'

def record_winner(winner):
    with open(LOG_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['Winner', 'Timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(LOG_FILE_PATH) == 0:
            writer.writeheader()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow({'Winner': winner, 'Timestamp': timestamp})

def record_game_data(player1, player2, winner, total_moves):
    with open(LOG_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['Player1', 'Player2', 'Winner', 'TotalMoves', 'Timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(LOG_FILE_PATH) == 0:
            writer.writeheader()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow({'Player1': player1, 'Player2': player2, 'Winner': winner, 'TotalMoves': total_moves, 'Timestamp': timestamp})

# Your existing game code remains unchanged

# ...

# In your TicTacToeGame class, where the game ends, call the record_winner and record_game_data functions:

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = make_empty_board()
        self.current_player = 'X'
        self.player1 = player1
        self.player2 = player2

    def play_game(self):
        total_moves = 0
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
                    total_moves += 1

                    if winner:
                        print_board(self.board)
                        print(f"Player {winner} wins!")
                        record_winner(winner)
                        record_game_data("HumanPlayer" if self.current_player == 'X' else "BotPlayer",
                                         "BotPlayer" if self.current_player == 'X' else "HumanPlayer",
                                         winner, total_moves)
                        break
                    elif is_full(self.board):
                        print_board(self.board)
                        print("It's a draw!")
                        record_game_data("HumanPlayer", "BotPlayer", 'Draw', total_moves)
                        break

                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                else:
                    print("Position is taken, try again.")
            except ValueError as e:
                print(str(e))
