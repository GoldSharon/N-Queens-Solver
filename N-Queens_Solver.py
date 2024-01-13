# Prompting the user to enter the number of queens
N = int(input("Enter the number of queens = "))

# Chessboard NxN matrix with all elements initialized to 0
board = [[0] * N for _ in range(N)]

def is_attack(i, j):
    # Checking if there is a queen in the same row or column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Checking diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queen(n):
    # If n is 0, a solution is found
    if n == 0:
        return True

    for i in range(0, N):
        for j in range(0, N):
            # Checking if we can place a queen here or not
            # A queen will not be placed if the place is being attacked or already occupied
            if (not is_attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                # Recursion: checking if we can put the next queen with this arrangement or not
                if N_queen(n - 1):
                    return True
                # If placing the queen in the current position doesn't lead to a solution, backtrack
                board[i][j] = 0
    return False

# Calling the N_queen function to find a solution
N_queen(N)

# Printing the final board configuration with queen placements
print("The positions to keep queens are:")
for i in board:
    print(i)
