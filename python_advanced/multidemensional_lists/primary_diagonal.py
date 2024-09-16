rows = int(input())
matrix = [[int(el) for el in input().split()] for row in range(rows)]

diagonal_sums = 0

for diagonal in range(rows):
    diagonal_sums += matrix[diagonal][diagonal]

print(diagonal_sums)