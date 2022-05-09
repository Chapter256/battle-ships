# Battleships game legend 
# X for placing battleship and hitting battleship
# ' ' for all available space 
# ' - ' for missed shots 

from random import randint

HIDDEN_BOARD = [[''] * 8 for x in range(8)]
GUESS_BOARD = [[''] * 8 for x in range(8)]
LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print(' A B C D E F G H')
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

def get_ship_location():
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8')
    column = input('Please enter a ship row a-h')
    while column not in 'abcdefgh':
        print('Please enter a valid column')
        column = input('Please enter a ship column a-h')
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to Battleships')
    print__board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You already guessed that')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Congrats! You hit a battleship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You missed!')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congrats, you have sunk all the battleships!')
        break
    print('You have' + str(turns) + 'turns remaining')
    if turns == 0: 
        print('Game Over')
        break