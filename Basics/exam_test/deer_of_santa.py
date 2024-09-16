import math

santa_days_missing = int(input())
left_food = int(input())
food_for_first_deer_for_day = float(input())
food_for_second_deer_for_day = float(input())
food_for_third_deer_for_day = float(input())

sum_for_first_deer = food_for_first_deer_for_day * santa_days_missing
sum_for_second_deer = food_for_second_deer_for_day * santa_days_missing
sum_for_third_deer = food_for_third_deer_for_day * santa_days_missing
sum_for_all = sum_for_first_deer + sum_for_second_deer + sum_for_third_deer

if left_food > sum_for_all:
    difference_down = math.floor(left_food - sum_for_all)
    print(f"{difference_down} kilos of food left.")
else:
    difference_up = math.ceil(sum_for_all - left_food)
    print(f"{difference_up} more kilos of food are needed.")
