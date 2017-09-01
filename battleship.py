'''
Created on 01/09/2017

@author: Ulises Lugo Fletes
'''

from random import randint  # Libreria que genera numeros aleatorios


def print_board(board):  # Imprimir el tablero separado por espacios
    for row in board:
        print " ".join(row)


def random_row(board):  # Fila aleatoria
    return randint(0, len(board) - 1)


def random_col(board):  # Columna aleatoria
    return randint(0, len(board[0]) - 1)


board = []

# Agrega a la lista caracteres
for x in range(0, 5):
    board.append(["O"] * 5)

print "Welcome to the Battleship single game"
print "This is the board and somewhere I have put a boat "
print_board(board)
print "Try to guess in which row and column is to beat me! You have 5 chances"


ship_row = random_row(board)
ship_col = random_col(board)


turn = 1

for n in range(5):
    print
    print "Turn %d" % (turn)
    # Pide las posibles soluciones y les resta 1 porque python considera la
    # fila 1 como 0
    guess_row = int(raw_input("Guess Row (vertical): "))
    guess_col = int(raw_input("Guess Col (horizontal): "))
    guess_row -= 1
    guess_col -= 1
    # Evalua si se adivino la ubicacion
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    # Evalua si no se adivino la ubicacion
    else:
        turn += 1  # contador para intentos
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print
        print_board(board)
        if turn == 6:
            print "Game Over"
