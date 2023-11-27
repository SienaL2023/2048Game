# this is the file that contains all the logic in the game
import random

# make function that initializes a game/grid at the start
def start_game():
    # [0  0  0  0]
    # [0  0  0  0]
    # [0  0  0  0]
    # [0] [0] [0] [0]
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    # print instructions for game
    print("These are the commands for this game:")
    print("W: Move up")
    print("A: Move left")
    print("S: Move down")
    print("D: Move right")

    add_new_2(mat)
    return mat

# choose random row/column
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)

    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


def get_current_state(mat):
    # check if game is won or not
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return 'WON'
            if(mat[i][j] == 0):
                return 'GAME NOT OVER'
    # no cell is empty,
    # but any moves in all directions
    # cells can merge and create empty cell
    for i in range(3): # checks just three rows
        for j in range(3): # checks just four columns
            if (mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i+1][j]):
                return 'GAME NOT OVER'
    # checking last row
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return 'GAME NOT OVER'
    # checking last column
    for i in range(3):
        if (mat[i][3] == mat[i+1][3]):
            return 'GAME NOT OVER'
    return 'LOST' # when none of the conditions r met

# function to compress the grid, after every step before and after merging cells
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    # loop to traverse through the rows
    # and move every cell as left as possible
    for i in range(4):
        pos = 0
        for j in range(4):
            if(mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]
                if(j != pos):
                    changed = True
                pos += 1
    return new_mat, changed


# function to merge the cells in matrix before compressing
# this just does the math not the movement
def merge(mat):
    changed = False
    for i in range(4): # all the numbers bc four colmuns
        for j in range(3): # 3 bc theres a plus one so u get the one next to it
            # checks if elemnts r same and not zero
            if(mat [i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0 # one becomes double while one becomes zero
                changed = True
    return mat, changed

# this is a function to reverse the matrix
def reverse(mat):
    # 2D array
    new_mat = []
    for i in range(4):
        new_mat.append([]) # this part makes the 1d new_mat thats blank into a 2d map with multiple rows!
        for j in range(4):
            new_mat[i].append(mat[i][3-j]) # new_mat i means that specific row ur changing
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i]) # basically this is uses the range
            # so cont from comment above
            # first time around, i = 0 j = 0, number thats in pos 0, 0 moves to pos 0 ,0,
            # second time, i = 0, j = 1, number in pos 0 , 1 moves to 1, 0 bc i and j switch
            # 3rd time, i= 0 j = 2 num in pos 0,2 moves to pos 2,0
    return new_mat
# function to update matrix if we move left
def move_left(mat):
    # first compress the mat
    new_mat, changed1 = compress(mat)
    # merge the cells
    new_mat, changed2 = merge(new_mat)

    changed = changed1 or changed2
    # compress again after merging bc if its 2 2 2 -> 4 0 2 -> 4 2 0
    new_mat, temp = compress(new_mat)

    return new_mat, changed

# function to update matrix if we move right
def move_right(mat):
    # first reverse the matrix
    new_mat = reverse(mat)
    # compress and merge but its like going left so reverse again
    new_mat, changed = move_left(new_mat)
    # reverse again
    new_mat = reverse(new_mat)

    return new_mat, changed

    # 4 2 2 2 --> 0 4 2 4
    # reverse -> 2 2 2 4
    # move left --> 4 2 4 0
    # reverse again --> 0 4 2 4

def move_up(mat):
    # transpose
    new_mat = transpose(mat)
    # move left
    new_mat, changed  = move_left(new_mat)
    # transpose
    new_mat = transpose(new_mat)
    return new_mat, changed

def move_down(mat):
    # transpose
    # move right
    # transpose
    new_mat = transpose(mat)
    new_mat, changed = move_right(new_mat)
    new_mat = transpose(new_mat)
    return new_mat, changed