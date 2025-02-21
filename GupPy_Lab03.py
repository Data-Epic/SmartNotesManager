# NAME: Yusuf Abdiwali Hussein


# PROBLEM 1: Placing tiles in a column until the edge of the board is reached

# Choose a random starting column and row
col = roll() % 6 + 1  # Generates a random column in {1, 2, 3, ..., 6}
row = (roll() % 6) * 2 + 2  # Generates a random row in {2, 4, 6, 8, 10, 12}

# Determine direction based on die roll
direction = 2 if roll() % 2 == 0 else -2  # Move up if even, down if odd

# Place the first tile
tile = Tile(RANDOM)
tile.place(col, row)

# Continue placing tiles until the edge of the board is reached
while 0 < row <= 12:
    row += direction  # Move up or down
    if row > 12 or row < 0:  # Stop if out of bounds
        break
    tile.place(col, row)

# PROBLEM 2: Placing tiles in a staggered row

# Roll to determine number of tiles and pattern type
num_tiles = roll()  # Number of tiles to place
pattern_type = roll()  # Determines pattern A or B

# Initial placement
col = 0
row = 6
alternate_row = 8 if pattern_type in [1, 2, 3] else 4  # Pattern A uses 8, Pattern B uses 4

# Place tiles in a staggered row
count = 0
while count < num_tiles:
    tile = Tile(RANDOM)
    tile.place(col, row)

    # Alternate rows
    row = alternate_row if row == 6 else 6
    col += 1  # Move right
    count += 1


# PROBLEM 3: Placing tiles in a row until the edge of the board is reached

# Choose a random starting row and column
row = roll() % 6 + 1  # Generates a random row in {1, 2, 3, ..., 6}
col = roll() % 11 + 2  # Generates a random column in {2, 3, 4, ..., 12}

# Determine direction
direction = -1 if col >= 6 else 1  # Left if col >= 6, right otherwise

# Place the first tile using a PIN
pin = PIN1
pin.place(col, row)

# Counting while loop to place tiles without going off the board
while 0 < col <= 12:
    col += direction  # Move left or right
    if col < 0 or col > 12:  # Stop if out of bounds
        break
    tile = Tile(RANDOM)
    tile.place(col, row)
