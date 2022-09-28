# Battleships game legend
# '_' for all available space
# '-' for missed shots
# 'X' for placing battleship and hitting battleship

from random import randint

HIDDEN_BOARD = [[''] * 8 for x in range(8)]
GUESS_BOARD = [[''] * 8 for x in range(8)]
LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
USERNAME = ''

def print_board(board):
    print('  A B C D E F G H')
    row_number = 1
    for row in board:
        print("%d|_%s|" % (row_number, "|_".join(row)))
        row_number += 1

def create_ships(board):
    for _ in range(10):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'
      
def fill_in_blanks(board):
    for row_num in range (len(board)):
        for col_num in range (len(board)):
            val = board[row_num] [col_num]
            if val != 'X' and val != '-':
                board[row_num] [col_num] = '_'
 
def get_ship_location():
    row = input('Please choose the row you want to strike (any number 1-8):\n')
    while row not in '12345678':
        print('Invalid row')
        row = input('Please choose the row you want to strike (any number 1-8):  \n')
    column = input('Please choose the letter of the column you want to strike (any letter a-h):  \n')
    column = column.upper()
    if column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H').upper()
    return int(row) - 1, LETTERS_TO_NUMBERS[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def valid_username(username):
    length = len(username)
    if length > 15 or length < 1: 
        return False
    return True

def setup_new_game():
    print('Welcome to Battleships')
    username = ''
    while username == '':
        input_name = input('Please enter your username:  ')
        if valid_username(input-name):
            username = input_name
            
    USERNAME = username

create_ships(HIDDEN_BOARD)
fill_in_blanks(HIDDEN_BOARD)
fill_in_blanks(GUESS_BOARD)

setup_new_game()

def play_game():
turns = 10
while turns > 0:
    print_board(HIDDEN_BOARD)
    print_board(GUESS_BOARD)
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
    print('You have' + str(turns) + ' turns remaining')
    if turns == 0: 
        print('Game Over')
        break
    
play_game()