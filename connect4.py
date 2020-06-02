### install dependencies
# numpy & pygame

### load packages
import numpy as np
import sys
# import pygame
import math

### global variables
ROW_COUNT = 6
COLUMN_COUNT = 7

### define helper functions
# create matrix style board
def create_board():
    # define 6x7 matrix
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    # what to return when function called
    return board

# drop piece in board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# check if choice is valid by passing board and column in it
def is_valid_location(board, col):
    # if top row is 0 after turn
    return board[ROW_COUNT-1][col] == 0

# check to see which row piece will fall on
def get_next_open_row(board, col):
    # for loop so that if row is 0 return that row
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# board allignment
def print_board(board):
    print(np.flip(board, 0))

# init board 
board = create_board()
# print board to show board
print_board(board)
# init game_over as false
game_over = False
# init turn starting at 0 count
turn = 0


# create game loop that runs while game is not over
while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make Your Selection (0-6):"))
        # if open col then find next open row and drop piece for player 1
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
    # ask player 2 input
    else:
        col = int(input("Player 2 Make Your Selection (0-6):"))
        # if open col then find next open row and drop piece for player 1
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)    
    # after player 2 goes then print the board
    print_board(board)
    # at end of turn increase turn count by 1
    turn += 1
    # determine if odd or even by taking turn divide by two and calc remainder. If no remainder than even and player 1 turn, if remainder, then it must be odd and player 2 turn
    turn = turn % 2