cards = input()
team_a = 11
team_b = 11
list_with_cards = cards.split(" ")
list_with_cards = set(list_with_cards)
is_terminated = False
for cards in list_with_cards:
    if "A" in cards:
        team_a -= 1
    elif "B" in cards:
        team_b -= 1
    if team_b < 7 or team_a < 7:
        is_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")

if is_terminated:
    print("Game was terminated")