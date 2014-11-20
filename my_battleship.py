"""
    Version: 1.0
    Program: my_battleship

    This is my_battleship, the first program that I am going to write on my own
        (although it models a script from codeacademy)

"""

#Import randint function from random



#Create a list to act as the board for the game
board = []

#Populate the board with rows of "O" to act as the grid of 5 x 5
    #Use a for in range loop
for rows in range(0,5):
    board.append(["O"] * 5)

#Function that will print the blank board
def print_board(rows):
    for row in rows:
        print " ".join(row)

#Create random variables and hide battleships
from random import randint

random_row = randint(0,5)
random_col = randint(0,5)

board[random_row][random_col] = "X"

#Print the results to check the progress!!
print_board(board)