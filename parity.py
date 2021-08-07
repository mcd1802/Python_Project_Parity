import csv


def load_grid(csv_file_path):
    """Loads data from a csv file.

    Args:
        csv_file_path: string representing the path to a csv file.
    Returns:
        A list of lists, where each sublist is a line in the csv file.
    """
    pass
    mygrid = [] # Initialise grid

    with open(csv_file_path) as csv_file: # Open csv file
        readcsv = csv.reader(csv_file)
        for line in readcsv: # read csv line by line
            mygrid.append(line) # add row into grid
    
    return (mygrid)

def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new column added.
    """
    pass

    for row in range(0,len(grid)): # Loop through rows
        check = 0 # reset counter
        for col in range(0,len(grid[row])): # Loop through columns
            if (grid[row][col] == "X"): # Count "X" in a row
                check = check + 1 # increase counter
        if ((check % 2) == 0): # if even then set "O"
            grid[row].append("O")
        else:                  # if not even then set "X"
            grid[row].append("X")

    return (grid)

def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new row added.
    """
    pass
    
    rows = len(grid) # get the number of rows

    if (rows>0): # Check if not an empty grid
        cols = len(grid[0])
        grid.extend([["O"] * cols])

        for col in range(0,cols): # Loop through the columns
            check = 0 # reset counter
            for row in range(0,rows):
                if (grid[row][col] == "X"): # Count "X" in a column
                    check = check + 1 # increase counter
            if ((check % 2) == 1):
                grid[rows][col] = "X"

    return (grid)

def flip_cell(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.

        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = x: 0, y: 0
            b = x: 1, y: 0
            c = x: 0, y: 1
            d = x: 1, y: 1

    Returns:
        The same grid, with a cell switched.
    """
    pass

    if (len(grid)>0): # check if grid not empty
        if ((x_pos >=0) and (x_pos < len(grid[0]))): # check if x_pos within columns range
            if ((y_pos >=0 and (y_pos < len(grid)))): # check if y_pos within rows range
                if (grid[y_pos][x_pos] == "O"):
                    grid[y_pos][x_pos] = "X" # Flip to "X"
                else:
                    grid[y_pos][x_pos] = "O" # Flip to "O"

    return (grid)

def find_flipped_cell(grid):
    """Determines which cell/cell in the grid was flipped.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        A list containing the coordinates of the cell with the flipped cell.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 0)
            b = (1, 0)
            c = (0, 1)
            d = (1, 1)
        If 'a' was the flipped letter, this function would return: [0, 0]
    """
    pass

    rows = len(grid) # number of rows of the grid
    pos = [None] * 2 # Initialise a list with two [None] values

    if (rows>0): # check if grid is not empty
        rflip = -1  # initialise row pos
        cflip = -1  # initialise column pos
        # Find row that is flipped
        for row in range(0,rows):
            check = 0 # reset counter
            for col in range(0,len(grid[0])):
                if (grid[row][col]=="X"): # count the number of "X" in a row
                    check = check + 1
            if ((check % 2)==1): # check if the number of "X" in the row is odd
                rflip = row # record the row
                row = rows  # finish the loop

        # Find column that is flipped
        for col in range(0,len(grid[0])):
            check = 0 # reset counter
            for row in range(0,rows):
                if(grid[row][col]=="X"): # count the number of "X" in a column
                    check = check + 1
            if ((check % 2)==1):
                cflip = col # record the column
                col = len(grid[0]) # finish the loop
        
        if ((rflip>-1) and (cflip>-1)): # If cell position is found
            pos[0] = cflip # set x pos
            pos[1] = rflip # set y pos

    return(pos)