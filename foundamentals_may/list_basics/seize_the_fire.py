fires = input().split("#")
water = int(input())

high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
effort = 0
total_fire = 0
print_list_for_values = []
is_put_out_the_fire = False

for fire in fires:
    type_of_fire = fire.split(" = ")
    value = int(type_of_fire[1])
    is_put_out_the_fire = False
    if water < value:
        break
    if value in high:
        if type_of_fire[0] == "High":
            is_put_out_the_fire = True
    elif value in medium:
        if type_of_fire[0] == "Medium":
            is_put_out_the_fire = True
    elif value in low:
        if type_of_fire[0] == "Low":
            is_put_out_the_fire = True

    if is_put_out_the_fire:
        water -= value
        effort += value * 0.25
        total_fire += value
        print_list_for_values.append(value)


print("Cells:")
for fire_cells in print_list_for_values:
    print(f"- {fire_cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")