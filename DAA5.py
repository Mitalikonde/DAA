def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # If all queens are placed, return True
    if col >= len(board):
        return True

    # Try placing a queen in each row of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack if placing queen didn't work

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

# Set board size
n = 8
board = [[0] * n for _ in range(n)]
board[0][0] = 1  # Place the first Queen

# Start placing the remaining queens
if solve_n_queens(board, 1):
    print_board(board)
else:
    print("No solution exists")
