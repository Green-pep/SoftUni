def calculator(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result

operator_for_calculation = input()
first_number = int(input())
second_number = int(input())

print(calculator(operator_for_calculation, first_number, second_number,))
