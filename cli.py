def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(" | ".join(str(cell) if cell is not None else " " for cell in row))
        print("-" * 9)

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for i in range(3):
        # Check horizontal wins
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

        # Check vertical wins
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check diagonal wins
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'X' if player == 'O' else 'O'

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    while winner is None:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] is None:
            board[row][col] = current_player
            winner = get_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if all(cell is not None for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break

            current_player = other_player(current_player)
        else:
            print("That position is already taken. Try again.")
