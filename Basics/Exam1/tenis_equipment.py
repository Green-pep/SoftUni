import math

price_racket = float(input())
count_rackets = int(input())
count_sockets = int(input())

amount_for_all_rackets = price_racket * count_rackets
price_sockets = price_racket / 6
amount_for_all_sockets = count_sockets * price_sockets
sum_of_all = amount_for_all_rackets + amount_for_all_sockets
price_of_other_stuff = sum_of_all * 0.2

sum_of_all += price_of_other_stuff

price_for_grigor = sum_of_all * 0.125     #1/8
price_for_sponsors = sum_of_all * 0.875   #7/8

print(f"Price to be paid by Djokovic {math.floor(price_for_grigor)}")
print(f"Price to be paid by sponsors {math.ceil(price_for_sponsors)}")