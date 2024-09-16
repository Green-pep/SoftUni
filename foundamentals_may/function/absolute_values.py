numbers = input().split()
absolute_numbers = []

for number in numbers:
    absolute_numbers.append(abs(float(number)))
print(absolute_numbers)