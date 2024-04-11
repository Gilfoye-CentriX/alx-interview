#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve_util(row):
        if row == N:
            solutions.append([row for row in board])
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0
    
    solve_util(0)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter the number of queens (N >= 4): "))
            if N < 4:
                print("N must be at least 4")
            else:
                break
        except ValueError:
            print("N must be a number")
    
    solve_n_queens(N)
