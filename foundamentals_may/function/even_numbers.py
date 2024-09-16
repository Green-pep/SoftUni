def is_even_number(checking_number):
    return checking_number % 2 == 0

numbers = input().split()
all_numbers = []
for number in numbers:
    number = int(number)
    all_numbers.append(number)

result = list(filter(is_even_number, all_numbers))
print(result)
