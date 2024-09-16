rows, columns = map(int, input().split())

start_matrix = ord("a")

for row in range(rows):
    for col in range(columns):
        print(f"{chr(start_matrix + row)}{chr(start_matrix + row + col)}{chr(start_matrix + row)}", end=' ')
    print()