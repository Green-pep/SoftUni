numbers = [0, 1]

while True:
    new_number = numbers[-1] + numbers[-2]
    numbers.append(new_number)
    if len(numbers) == 100:
        break
print(numbers)