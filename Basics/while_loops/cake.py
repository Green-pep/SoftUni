length_cake = int(input())
width_cake = int(input())

count_pieces = length_cake * width_cake
is_cake_enough = True
command = input()

while command != "STOP":
    pieces = int(command)
    count_pieces -= pieces
    if count_pieces <= 0:
        is_cake_enough = False
        break
    command = input()

if is_cake_enough:
    print(f"{count_pieces} pieces are left." )
else:
    print(f"No more cake left! You need {abs(count_pieces)} pieces more.")