n = int(input())

odd_numbers = 0
even_numbers = 0
difference = 0

for position in range(n):

    number = int(input())

    if position % 2 == 0:
        even_numbers += number
    else:
        odd_numbers += number

difference = abs(even_numbers - odd_numbers)
if difference:
    print(f"No")
    print(f"Diff = {difference}")
else:
    print('Yes')
    print(f"Sum = {even_numbers}")
