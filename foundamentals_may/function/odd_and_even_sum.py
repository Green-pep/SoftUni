def sum_of_odd_and_even_numbers(number):
    number.split()
    odd_numbers = []
    even_numbers = []
    for numbers in number:
        numbers = int(numbers)
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        else:
            odd_numbers.append(numbers)
    print(f"Odd sum = {sum(odd_numbers)}, Even sum = {sum(even_numbers)}")


single_number = input()
sum_of_odd_and_even_numbers(single_number)