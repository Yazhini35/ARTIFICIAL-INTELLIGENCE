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
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row (0, 1, or 2) for player {}: ".format(player)))
        col = int(input("Enter column (0, 1, or 2) for player {}: ".format(player)))

        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)

            if check_winner(board):
                print("Player {} wins!".format(player))
                break

            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a tie!")
                break

            player = 'X' if player == 'O' else 'O'
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
