rows, columns = map(int, input().split(", "))
matrix = [[int(el) for el in input().split(", ")] for row in range(rows)]
max_number = float("-inf")

for row in range(rows - 1):
    for column in range(columns - 1):
        first_number = matrix[row][column]
        second_number = matrix[row][column + 1]
        third_number = matrix[row + 1][column]
        fourth_number = matrix[row + 1][column + 1]
        sum_quarter = sum([first_number, second_number,third_number,fourth_number])
        if sum_quarter > max_number:
            max_number = sum_quarter
            numbers = ([first_number, second_number], [third_number, fourth_number])

print(*numbers[0])
print(*numbers[1])
print(max_number)