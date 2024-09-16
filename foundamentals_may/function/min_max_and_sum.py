numbers = input().split()
number_as_digits = []
for number in numbers:
    number = int(number)
    number_as_digits.append(number)
min_numbers = min(number_as_digits)
max_numbers = max(number_as_digits)
sum_numbers = sum(number_as_digits)

print(f"The minimum number is {min_numbers}")
print(f"The maximum number is {max_numbers}")
print(f"The sum number is: {sum_numbers}")