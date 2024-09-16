rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for row in range(rows)]

flattened_matrix = [el for row in matrix for el in row]

print(flattened_matrix)