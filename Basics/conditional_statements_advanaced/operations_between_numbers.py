first_number = int(input())
second_number = int(input())
operator = input()
result = 0

if operator == "-" or operator == "+" or operator == "*":
    odd_or_even = 0
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    if result % 2:
        odd_or_even = "odd"
    else:
        odd_or_even = "even"
    print(f'{first_number} {operator} {second_number} = {result} - {odd_or_even}')
elif operator == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f'{first_number} / {second_number} = {result} ')
elif operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f'{first_number} % {second_number} = {result}')
