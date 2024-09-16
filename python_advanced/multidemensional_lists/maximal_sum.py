rows, cols = map(int, input().split())
matrix = [[int(el) for el in input().split()]for _ in range(rows)]

max_sum = float("-inf")
first_index_row = 0
first_index_col = 0

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = 0
        for z in range(i, i + 3):
            for y in range(j, j + 3):
                current_sum += matrix[z][y]
        if current_sum > max_sum:
            max_sum = current_sum
            first_index_row = i
            first_index_col = j


print(f'Sum = {max_sum}')
submatrix = [matrix[row][first_index_col:first_index_col + 3] for row in range(first_index_row, first_index_row + 3)]
[print(*row) for row in submatrix]