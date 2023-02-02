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


def try_to_place_ship_on_grid(row, col, direction, length):
    """Based on direction, will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
  
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """Will create a 10x10 grid and randomly place down ships 
    of different sizes in diffrent directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)
   
    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, col - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randit(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
         
def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet
    
    debug_mode = True
    
    alphabet = alphabet[0: len(grid) + 1]
    
    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "0":
                if debug_mode:
                    print("0", end=" ")
                else:
                    print("0", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")
    print(" ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")