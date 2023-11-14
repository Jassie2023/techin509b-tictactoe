def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


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
    def make_move(board):
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number.")

                
class BotPlayer:
    def make_move(board):
        import random
        return random.randint(0, 2), random.randint(0, 2)


if __name__ == '__main__':
    human_player = HumanPlayer()
    bot_player = BotPlayer()
    game = TicTacToeGame(player1=human_player, player2=bot_player)
    game.play_game()
