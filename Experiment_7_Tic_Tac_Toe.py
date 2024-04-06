# Program to play tic tac toe with AI in python

import random

def print_board(board):
    print("  1 2 3")
    print("  -----")
    for i in range(3):
        print(i+1, end="|")
        for j in range(3):
            print(board[i][j], end="|")
        print("\n  -----")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "O"
            score = minimax(board, depth+1, False)
            board[cell[0]][cell[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "X"
            score = minimax(board, depth+1, True)
            board[cell[0]][cell[1]] = " "
            best_score = min(score, best_score)
        return best_score
    
def get_best_move(board):
    best_score = -1000
    best_move = (-1, -1)
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = "O"
        score = minimax(board, 0, False)
        board[cell[0]][cell[1]] = " "
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        x, y = map(int, input("Enter your move (row column): ").split())
        if board[x-1][y-1] != " ":
            print("Invalid move, try again")
            continue
        board[x-1][y-1] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        move = get_best_move(board)
        board[move[0]][move[1]] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("You lose!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()

