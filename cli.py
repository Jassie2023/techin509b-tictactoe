# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board

# Reminder to check all the tests

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        # Check horizontal wins
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

        # Check vertical wins
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        winner = 'X'  # FIXME
        current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already taken. Try again.")
