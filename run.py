import random

# Battleships game legend
# ' _ ' for all empty space
# ' * ' for missed shots
# ' X ' for hitting part of a ship
# ' 0 ' for part of a ship

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for number of ships to place
num_of_ships = 8
# Global variable for bullets left
bullets_left = 50
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there."""
    global grid
    global ship_positions
    
    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ",":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "0"
    return all_valid