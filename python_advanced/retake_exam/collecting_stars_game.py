matrix = [input().split() for _ in range(int(input()))]

collected_stars = 2
player_failed = False
player_position = next((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == 'P')

while True:
    command = input()
    x, y = player_position
    old_x, old_y = x, y
    if command == 'left':
        y -= 1
    elif command == 'right':
        y += 1
    elif command == 'up':
        x -= 1
    elif command == 'down':
        x += 1

    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
        x, y = 0, 0

    cell = matrix[x][y]
    if cell == "*":
        collected_stars += 1

    elif cell == "#":
        collected_stars -= 1
        x, y = player_position
    else:
        matrix[player_position[0]][player_position[1]] = "."

    if collected_stars <= 0:
        player_failed = True
        break

    matrix[old_x][old_y] = "."
    matrix[x][y] = "P"
    player_position = (x, y)
    if collected_stars == 10:
        break

if not player_failed:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")
for row in matrix:
    print(' '.join(row))
