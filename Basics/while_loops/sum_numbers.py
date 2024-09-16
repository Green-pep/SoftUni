first_number = int(input())
counter = 0

while True:
    numbers = int(input())
    counter += numbers
    if counter >= first_number:
        break
print(counter)
