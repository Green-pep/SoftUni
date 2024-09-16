country = input()
type_of_gymnastic = input()

hardness = 0
performance = 0

if country == "Russia":
    if type_of_gymnastic == "ribbon":
        hardness += 9.100
        performance += 9.400
    elif type_of_gymnastic == "hoop":
        hardness += 9.300
        performance += 9.800
    else:
        hardness += 9.600
        performance += 9.000

if country == "Bulgaria":
    if type_of_gymnastic == "ribbon":
        hardness += 9.600
        performance += 9.400
    elif type_of_gymnastic == "hoop":
        hardness += 9.550
        performance += 9.750
    else:
        hardness += 9.500
        performance += 9.400

if country == "Italy":
    if type_of_gymnastic == "ribbon":
        hardness += 9.200
        performance += 9.500
    elif type_of_gymnastic == "hoop":
        hardness += 9.450
        performance += 9.350
    else:
        hardness += 9.700
        performance += 9.150

amount_of_all_points = hardness + performance
more_points_to_the_max = 100 - (amount_of_all_points / 20 * 100)


print(f"The team of {country} get {amount_of_all_points:.3f} on {type_of_gymnastic}.")
print(f"{more_points_to_the_max:.2f}%")
