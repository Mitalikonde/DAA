Design n-Queens matrix having first Queen placed. Use backtracking to place remaining 
Queens to generate the final n-queen’s matrix. 


def print_board(board):
    """Helper function to print the board."""
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """Utilizes backtracking to place queens and solve the n-Queens problem."""
    # If all queens are placed, return True
    if col >= n:
        return True

    # Try placing queen in all rows in the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1
            
            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] leads to a solution, return True
            # If it doesn’t lead to a solution, backtrack (remove the queen)
            board[i][col] = 0

    return False

def initialize_board(n, first_row, first_col):
    """Initialize the board with the first queen placed at (first_row, first_col)."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[first_row][first_col] = 1
    return board

def solve_n_queens_with_initial(n, first_row, first_col):
    """Main function to solve n-Queens with the first queen placed."""
    board = initialize_board(n, first_row, first_col)
    
    # Start placing remaining queens from the next column
    if solve_n_queens(board, 0 if first_col != 0 else 1, n):
        print("Solution for n-Queens:")
        print_board(board)
    else:
        print("No solution exists.")

# Example usage
n = 8  # Size of the board (8x8)
first_row, first_col = 0, 0  # Initial position of the first queen
solve_n_queens_with_initial(n, first_row, first_col)


# Output:

# Solution for n-Queens:
# Q . . . . . . .
# . . . . . . Q .
# . . . . Q . . .
# . . . . . . . Q
# . Q . . . . . .
# . . . Q . . . .
# . . . . . Q . .
# . . Q . . . . .

# Time complexity : O(n!)
# Space complexity : O(n^2)
