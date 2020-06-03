### install dependencies
# numpy & pygame

### load packages
import numpy as np
import sys
import pygame
import math

### global variables
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
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
    # allignment in numpy package flip with 0 as xaxis position
    print(np.flip(board, 0))

# recognize a win
def winning_move(board, piece):
    # check all horizontal locations for horizontal win
    # loop over all columns (all but 3 columns can work for a win)
    for c in range(COLUMN_COUNT-3):
        # loop over all rows
        for r in range(ROW_COUNT):
            # if place in row has a piece and then 3 next over poisitons have a piece
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                # return true which ends game loop
                return True
    # check all vertical locations for vertical win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            # if place in row has a piece and then 3 next over poisitons have a piece
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                # return true which ends game loop
                return True
    # check for pos. sloped diags
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            # if place in row has a piece and then 3 next over poisitons have a piece
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                # return true which ends game loop
                return True
    # check fo neg. sloped diags
    for c in range(COLUMN_COUNT):
        for r in range(3, ROW_COUNT):
            # if place in row has a piece and then 3 next over poisitons have a piece
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                # return true which ends game loop
                return True

# function to draw board with pygame
def draw_board(board):
    # fill in background first
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # draw big blue rectangle below one solid black row
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draw circles in each row/column position
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    # fill in pieces 2nd based on what players pick
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            # make player 1 piece red
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            # make player 2 piece yellow
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()    

### initialize basic features of game
# init board 
board = create_board()
# print board with prevoiusly defined function to show board
print_board(board)
# init game_over as false
game_over = False
# init turn starting at 0 count
turn = 0

### init pygame and design feature
pygame.init()
# init radius for circles
RADIUS = int(SQUARESIZE/2 - 5)
# square size 100 pixels
SQUARESIZE = 100
# width of display
width = COLUMN_COUNT * SQUARESIZE
# height of display
height = (ROW_COUNT + 1) * SQUARESIZE
# size of display is a tuple of width and height
size = (width, height)
# init screen with pygame package functions
screen = pygame.display.set_mode(size)
# draw board
draw_board(board)
# update display pygame
pygame.display.update()
# init pygame font
myfont = pygame.font.SysFont("monospace", 75)


### Main loop to operate game
# create game loop that runs while game is not over
while not game_over:
    
    for event in pygame.event.get():
        # quit/exit feature
        if event.type == pygame.QUIT:
            sys.exit()
        
        # mouse scroll to see piece while moving mouse on top blank row
        if event.type == pygame.MOUSEMOTION:
            # draw black rectangle at top
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            # position is row 1
            posx = event.pos[0]
            # if player one turn -red (based on rem of 0)
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            # elese player 2 turn - yellow
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        # clickdown feature
        if event.type == pygame.MOUSEBUTTONDOWN:     
             # draw black rectangle at top
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            # use pygame to select column based on click
            # print(event.pos)
            # Ask for Player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # if open col then find next open row and drop piece for player 1
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    # if move hits a win, declare player 1 victory
                    if winning_move(board, 1):
                        # init victory label with pygame font
                        label = myfont.render("player 1 Wins!", 1, RED)
                        # update screen at coordinate 40,10 (top empty row)
                        screen.blit(label, (40,10))
                        game_over = True
            
            # ask player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # if open col then find next open row and drop piece for player 1
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)    
                    # if move hits a win, declare player 1 victory
                    if winning_move(board, 2):
                        # init victory label with pygame font
                        label = myfont.render("player 2 Wins!", 1, YELLOW)
                        # update screen at coordinate 40,10 (top empty row)
                        screen.blit(label, (40,10))
                        game_over = True
                        
                
        # after player 2 goes then print the board
        print_board(board)
        draw_board(board)
        # at end of turn increase turn count by 1
        turn += 1
        # determine if odd or even by taking turn divide by two and calc remainder. If no remainder than even and player 1 turn, if remainder, then it must be odd and player 2 turn
        turn = turn % 2
        # on a win, wait 3 secs to shutdown
        if game_over:
            pygame.time.wait(3000)