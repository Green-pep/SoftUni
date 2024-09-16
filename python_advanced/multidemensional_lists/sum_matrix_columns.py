rows, columns = map(int, input().split(", "))

matrix = [[int(el) for el in input().split()] for row in range(rows)]


for column in range(columns):
    sum_numbers = 0
    for row in range(rows):
        sum_numbers += matrix[row][column]
    print(sum_numbers)
