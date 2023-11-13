# 2048

# 4 x 4 grid with directions to move um down left or right
import logic
# creates mat, starts game
mat = logic.start_game()
for x in mat:
    print(x)

print("")
# moves left
mat2, temp = logic.move_left(mat)
# adds 2
logic.add_new_2(mat2)
# moves the 2 to the left
mat2, temp = logic.move_left(mat2)
for x in mat2:
    print(x)
print("this is main!")
