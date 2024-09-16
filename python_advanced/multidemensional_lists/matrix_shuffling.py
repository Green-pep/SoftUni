def validate_columns(r, c, rows1, cols1):
    return 0 <= r < rows1 and 0 <= c < cols1


rows, columns = map(int, input().split())

matrix = [[el for el in input().split()] for row in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue
    old_row, old_column = int(command[1]), int(command[2])
    new_row, new_column = int(command[3]), int(command[4])
    if validate_columns(old_row, old_column, rows, columns) and validate_columns(new_row, new_column, rows, columns):
        matrix[old_row][old_column], matrix[new_row][new_column] = matrix[new_row][new_column], matrix[old_row][old_column]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


