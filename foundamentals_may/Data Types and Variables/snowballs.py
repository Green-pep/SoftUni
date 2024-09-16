cont_of_balls_which_is_made = int(input())
best_result_ball = 0
best_weight_of_the_snowball = 0
best_time_needed = 0
best_quality = 0

for balls in range(cont_of_balls_which_is_made):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    sum_of_balls = (weight_of_the_snowball / time_needed) ** quality
    if sum_of_balls > best_result_ball:
        best_result_ball = sum_of_balls
        best_weight_of_the_snowball = weight_of_the_snowball
        best_time_needed = time_needed
        best_quality = quality

print(f"{best_weight_of_the_snowball} : {best_time_needed} = {int(best_result_ball)} ({best_quality})")