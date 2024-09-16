def progress(energy, day, water, food, peoples):

    needed_food = food / peoples

    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.3

    if day % 3 == 0:
        food -= needed_food
        energy += energy * 0.1
    return energy, water, food


def hunting_process(days, count_of_players, energy):
    is_enough_energy = True
    water_per_day_for_person = float(input())
    food_per_day_for_person = float(input())

    needed_water = (water_per_day_for_person * count_of_players) * days
    needed_food = (food_per_day_for_person * count_of_players) * days

    for day_ in range(1, days + 1):
        losing_energy = float(input())
        energy -= losing_energy
        if energy <= 0:
            is_enough_energy = False
            break
        energy, needed_water, needed_food = progress(energy, day_, needed_water, needed_food, players)

    if not is_enough_energy:
        print(f"You will run out of energy. You will be left with {needed_food:.2f} food and {needed_water:.2f} water.")

    else:
        print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")


days_of_adventure = int(input())
players = int(input())
group_energy = float(input())

hunting_process(days_of_adventure, players, group_energy)

