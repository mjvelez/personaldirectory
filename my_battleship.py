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
for rows in range(0, 5):
    board.append(["O"] * 5)

#Function that will print the blank board
def print_board(rows):
    for row in rows:
        print " ".join(row)

#Create random variables and hide battleships
from random import randint

random_row = randint(0, 4)
random_col = randint(0, 4)

board[random_row][random_col] = "X"

#Target location for debugging
print random_row
print random_col

#Guess where the battleships are
def guess_entry():
    turns = 3
    while turns > 0:
        guess_row = int(raw_input("Guess the row of the battleship: "))
        guess_col = int(raw_input("Guess the col of the battleship: "))

        if guess_row < 5 and guess_row >= 0 and guess_col < 5 and guess_col >= 0:
            hit = board[guess_row][guess_col]
            print hit
            if hit == "X":
                print "Arrrgggg, Ye sunk me battleship...."
                break
            else:
                print "Ye Missed! Try again ye scurvey devil ye!"
                turns -= 1
                if turns == 0:
                    print "Thee seas be mine! Arrgggggg!!!"
        else:
            print "That's not on the board... Let's start this turn over."


guess_entry()

#Print the results to check the progress!!
print_board(board)