number_of_cars = int(input())

cars_in_parking = set()
for _ in range(number_of_cars):
    command = input().split(", ")
    direction, reg_number = command[0], command[1]

    if direction == "IN":
        cars_in_parking.add(reg_number)
    else:
        if reg_number in cars_in_parking:
            cars_in_parking.remove(reg_number)

if cars_in_parking:
    print(*cars_in_parking, sep="\n")
else:
    print("Parking Lot is Empty")