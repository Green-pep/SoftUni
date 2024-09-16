actor_name = input()
academy_points = float(input())
count_ratings = int(input())

points = academy_points + 0

for ratings in range(count_ratings):
    if points > 1250.5:
        break
    jury_name = input()
    points_from_jury = float(input())
    points += ((len(jury_name) * points_from_jury) / 2)


difference = abs(points - 1250.5)

if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
