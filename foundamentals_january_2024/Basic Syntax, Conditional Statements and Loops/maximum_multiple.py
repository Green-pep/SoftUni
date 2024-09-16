divisor = int(input())
boundary = int(input())
is_found = False
found_number = 0

for number in range(boundary, divisor + 1, -1):
    if number % divisor == 0:
        found_number = number
        is_found = True
        break
print(found_number)
