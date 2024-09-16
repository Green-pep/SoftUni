number = input()
current_number = 0
last_number = 0
saved_number = 0

for i in range(len(number)):
    slice_number = number[i]
    current_number = slice_number
    slice_number = int(slice_number)
    if saved_number == 0:
        saved_number = int(current_number)
    elif int(last_number) > int(current_number):
        saved_number = str(saved_number) + str(slice_number)
    elif int(last_number) < int(current_number):
        saved_number = str(slice_number) + str(saved_number)
    last_number = int(current_number)

print(saved_number)