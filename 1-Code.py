def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board)):
        if all(board[row][col] == board[row + 1][col] == board[row + 2][col] != ' ' for row in range(len(board) - 2)):
            return True

    # Check diagonals
    if all(board[i][i] == board[i + 1][i + 1] == board[i + 2][i + 2] != ' ' for i in range(len(board) - 2)):
        return True
    if all(board[i][2 - i] == board[i + 1][1 - i] == board[i + 2][0 - i] != ' ' for i in range(len(board) - 2)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
