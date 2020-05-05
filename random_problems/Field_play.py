"""
You are given a matrix of the following characters: "R", "L", "U", "D". Yoko stands in the top-left cell (with the lowest index on both axes). Each turn Yoko goes to the neighbor cell using the character from current cell: Right for r, left for l, down for d and up for u. Find the cell, that Yoko reaches and after that gets out of bounds or determine, that such a cell does not exist. 
"""

def breaking_of_the_box(size = (10, 10), verbose = False):
    """
    Generating a field with randomly filled values 'R', 'L', 'U', 'D',
    which point moving direction of a player. Field is generated randomly at any call.
    :param: size: tuple, shape of a field
    :param: verbose: bool, if True, print player position at any moment of a game
    :returns: print state of the game, if player is breaks the field, or stucks in it
    """
    import numpy as np
    r, l, u, d = "R", "L", "U", "D" # initiating walkind directions
    np.random.seed(int(time.time()))
    
    # initiating field with walking directions
    field = np.random.randint(1, 5, size = (10, 10))
    field = np.where(field ==1, r, field)
    field = np.where(field =='2', l, field)
    field = np.where(field =='3', u, field)
    field = np.where(field =='4', d, field)

    i, j = 0, 0
    coordinates = []
    
    # iterating in a field
    while (i<field.shape[0] and i>-1) and (j<field.shape[1] and j>-1):
        prev_i,prev_j = i, j
        coordinates.append((i, j)) 
        
        copy_field = field.copy()
        
        if field[i][j] == r:
            j+=1
        elif field[i][j] == l:
            j-=1
        elif field[i][j] == u:
            i-=1
        elif field[i][j] == d:
            i+=1
        copy_field[i][j] = "X"
        if verbose == True:
            print(copy_field, "#"*48, sep = "\n") #printing step by step position of a player
        if (i, j) in coordinates:
            # in case of infitine loop break
            print("Player is stucked inside of a box")
            break

    else:
        print("Player came out of the box")
        print("Coordinates of a breaking point", "(", prev_i, prev_j, ")")
        
breaking_of_the_box(size = (8, 7),verbose = True)

