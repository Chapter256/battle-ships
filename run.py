# Battleships game legend 
# X for placing battleship and hitting battleship
# ' ' for all available space 
# ' - ' for missed shots 

from random import randint

HIDDEN_BOARD = [[''] * 8 for x in range(8)]
GUESS_BOARD = [[''] * 8 for x in range(8)]

letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def print_board(board): 
    print(' a b c d e f g h')
    print(' ---------------')
    row_number = 1 
    for row in board: 
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'
        
def count_hit_ships(): 
    pass 

create_ships()
turns = 10 
#while turns > 0: