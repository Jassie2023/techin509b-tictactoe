# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

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

def move_step(board, row, col, player):
    if board[row][col] is None:
        board[row][col] = player
        return True
    return False

def is_full(board):
    return all(cell is not None for row in board for cell in row)

if __name__ == '__main__':
    board = make_empty_board()
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if row not in (0, 1, 2) or col not in (0, 1, 2):
                raise ValueError("Invalid input. Row and column must be 0, 1, or 2.")

            if move_step(board, row, col, current_player):
                winner = get_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = 'X' if current_player == 'O' else 'O'
            else:
                print("Position is taken, you should try it again.")
        except ValueError as e:
            print(str(e))
    
