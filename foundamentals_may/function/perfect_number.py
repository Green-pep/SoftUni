def is_aliquot(number: int) -> str:
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    if number == sum_of_divisors:
        return "We have a perfect number!"
    return "It's not so perfect."


some_number = int(input())
print(is_aliquot(some_number))