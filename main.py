# 2048
# 4 x 4 grid with directions to move um down left or right
import logic as l

if __name__ == '__main__':
    # this will start the game with the initial mat
    mat = l.start_game()
    for m in mat:
        print(m)
while(True):
    # ask for user input
    x = input("press a command: ")
    if(x.upper() == 'W'):
        # call move up
        mat, flag = l.move_up(mat)
        # get current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if(status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break
    elif(x.upper() == "S"):
        # move downnnnnnn
        mat, flag = l.move_down(mat)
        # get current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break
    elif(x.upper() == 'A'):
        # move left
        mat, flag = l.move_left(mat)
        # get current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break
    elif(x.upper() == 'D'):
        mat, flag = l.move_right(mat)
        # get current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break

    else:
        print("Invalid key pressed, please try again!")
    for m in mat:
        print(m)