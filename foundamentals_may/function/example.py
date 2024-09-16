def factorial_calculator(number):
    for factorial in range(1, number):
        number *= factorial
    return number


first = int(input())
second = int(input())

first_number = factorial_calculator(first)
second_number = factorial_calculator(second)
result = first_number / second_number
print(f'{result:.2f}')