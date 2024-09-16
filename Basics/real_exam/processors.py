import math

needed_processors = int(input())
count_of_workers = int(input())
working_days = int(input())

working_hours = working_days * 8
sum_of_working_hours = count_of_workers * working_hours
crafted_processors = math.floor(sum_of_working_hours / 3)
price_for_one_processor = 110.10

if crafted_processors >= needed_processors:
    difference = crafted_processors - needed_processors
    profit = difference * price_for_one_processor
    print(f"Profit: -> {profit:.2f} BGN")
else:
    difference = needed_processors - crafted_processors
    losses = difference * price_for_one_processor
    print(f"Losses: -> {losses:.2f} BGN")