def factorial_division(first_number, second_number):
    first_factorial = 1
    second_factorial = 1
    for factorial in range(1, first_number + 1):
        first_factorial *= factorial
    for factorial in range(1, second_number + 1):
        second_factorial *= factorial
    result = first_factorial / second_factorial
    return result


first = int(input())
second = int(input())
print(f"{factorial_division(first, second):.2f}")

