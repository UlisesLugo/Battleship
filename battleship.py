'''
Created on 01/09/2017

@author: Ulises Lugo Fletes
'''

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

x = 1

for n in range(25):
    print
    guess_row = int(raw_input("Guess Row (vertical): "))
    guess_col = int(raw_input("Guess Col (horizontal): "))
    guess_row -= 1
    guess_col -= 1
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship! In %d tries" % (x)
        break
    else:
        x += 1
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print
        print_board(board)
