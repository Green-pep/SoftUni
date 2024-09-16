rows, cols = map(int, input().split())

matrix = [[el for el in input().split()] for _ in range(rows)]
identical_squares = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        current_char = matrix[i][j]
        next_char = matrix[i][j + 1]
        down_char = matrix[i + 1][j]
        diagonal_char = matrix[i + 1][j + 1]
        if current_char == next_char == down_char == diagonal_char:
            identical_squares += 1
print(identical_squares)