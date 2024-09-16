rows, columns = map(int, (input().split(", ")))

matrix = []
sum_numbers = 0
for row in range(rows):
    numbers = [int(el) for el in input().split(", ")]
    matrix.append(numbers)
    sum_numbers += sum(numbers)

print(sum_numbers)
print(matrix)
