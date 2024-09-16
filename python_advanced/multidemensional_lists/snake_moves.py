def fill_matrix_with_snake(rows, cols, snake):
    matrix = []
    snake_length = len(snake)
    index = 0

    for row in range(rows):
        current_row = []
        for col in range(cols):
            # Determine the position in the snake string
            current_row.append(snake[index % snake_length])
            index += 1

        # Reverse every second row to create a zigzag effect
        if row % 2 != 0:
            current_row.reverse()

        matrix.append(current_row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


# Read input
rows, cols = map(int, input().strip().split())
snake = input().strip()

# Fill the matrix with the snake's path
result_matrix = fill_matrix_with_snake(rows, cols, snake)

# Print the matrix
print_matrix(result_matrix)



