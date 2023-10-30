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
    add_new_2(mat)
    return mat

# choose random row/column
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)

    # check if empty before assigning num
    mat[r][c] = 2
