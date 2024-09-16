length_box = int(input())
width_box = int(input())
high_box = int(input())

free_space = length_box * width_box * high_box
is_enough_space = True
command = input()

while command != "Done":
    taken_boxes = int(command)
    free_space -= taken_boxes
    if free_space < 0:
        is_enough_space = False
        break
    command = input()

if is_enough_space:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")