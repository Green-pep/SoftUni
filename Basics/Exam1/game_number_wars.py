name_of_first_player = input()
name_of_second_player = input()

winner_name = ""
points_of_first_player = 0
points_of_second_player = 0

for dealings in range(0, 18+1):
    first_player_card = input()
    second_plyer_card = input()
    if first_player_card == "End of game" or second_plyer_card == "End of game":
        print(f"{name_of_first_player} has {points_of_first_player} points")
        print(f"{name_of_second_player} has {points_of_second_player} points")
        break

    if first_player_card > second_plyer_card:
        points_of_first_player += int(first_player_card) - int(second_plyer_card)
    elif second_plyer_card > first_player_card:
        points_of_second_player += int(second_plyer_card) - int(first_player_card)

    if first_player_card == second_plyer_card:
        points_of_first_player = 0
        points_of_second_player = 0

        first_player_card = input()
        second_plyer_card = input()

        if first_player_card > second_plyer_card:
            winner_name = name_of_first_player
            points_of_first_player += int(first_player_card) - int(second_plyer_card)
        elif second_plyer_card > first_player_card:
            winner_name = name_of_second_player
            points_of_second_player += int(second_plyer_card) - int(first_player_card)

        difference = abs(points_of_first_player - points_of_second_player)

        print(f"Number wars!")
        print(f"{winner_name} is winner with {difference} points")
        break



