first_player_name = input()
second_player_name = input()
cards_left = 36
points_of_first_player = 0
points_of_second_player = 0
winning_points = 0
is_number_war = False

while cards_left > 0:
    command = input()
    if command == "End of game":
        break
    first_player_card = int(command)
    second_player_card = int(input())
    cards_left -= 2
    winning_points = abs(first_player_card - second_player_card)

    if first_player_card > second_player_card:
        points_of_first_player += winning_points

    elif second_player_card > first_player_card:
        points_of_second_player += winning_points

    else:
        print("Number wars!")
        first_player_card = int(input())
        second_player_card = int(input())
        winning_points = abs(first_player_card - second_player_card)
        if first_player_card > second_player_card:
            print(f"{first_player_name} is winner with {winning_points} points")

        elif second_player_card > first_player_card:
            print(f"{first_player_name} is winner with {winning_points} points")

        is_number_war = True
        break

if not is_number_war:
    print(f"{first_player_name} has {points_of_first_player} points")
    print(f"{second_player_name} has {points_of_second_player} points")
