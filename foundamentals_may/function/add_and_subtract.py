def sum_numbers(first: int, second: int):
    sum_number = first + second
    return sum_number


def subtract(sum_number, third):
    final_result = sum_number - third
    return final_result


def add_and_subtract(first_number_of_numbers, second_number_of_numbers, third_number_of_numbers):
    sum_of_numbers = sum_numbers(first_number_of_numbers, second_number_of_numbers)
    result = subtract(sum_of_numbers, third_number_of_numbers)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
