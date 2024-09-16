import math

tournaments = int(input())
starting_points = int(input())

counter_points = 0
won_tournaments = 0

for _ in range(0, tournaments):
    status_tournament = input()
    if status_tournament == "W":
        won_tournaments += 1
        counter_points += 2000
    elif status_tournament == "F":
        counter_points += 1200
    else:
        counter_points += 720

average_points = counter_points / tournaments
sum_points = counter_points + starting_points
percentage_wins = (won_tournaments / tournaments) * 100

print(f"Final points: {sum_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_wins:.2f}%")
