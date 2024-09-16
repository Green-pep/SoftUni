def smallest_number(first_number: int, second_number: int, third_number: int) -> int:
    list_with_numbers = [first_number, second_number, third_number]
    return min(list_with_numbers)

first = int(input())
second = int(input())
third = int(input())

print(smallest_number(first, second, third))