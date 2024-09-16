rows = int(input())
matrix = []
for row in range(rows):
    elements = [el for el in input() for index in el]
    matrix.append(elements)
symbol = input()
is_symbol_match = False

for row in range(rows):
    for el in range(rows):
        if matrix[row][el] == symbol:
            is_symbol_match = True
            print(f"({row}, {el})")
            break
    if is_symbol_match:
        break
if not is_symbol_match:
    print(f'{symbol} does not occur in the matrix')
