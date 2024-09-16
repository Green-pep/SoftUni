numbers = input().split()
number_as_digits = []

for number in numbers:
    number = int(number)
    number_as_digits.append(number)

sorted_number = sorted(number_as_digits)
print(sorted_number)