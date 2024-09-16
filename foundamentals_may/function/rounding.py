def round_numbers(numbers):
    rounded_numbers = []
    for number in numbers:
        rounded_number = round(float(number))
        rounded_numbers.append(rounded_number)
    return rounded_numbers


n = input().split()
print(round_numbers(n))


