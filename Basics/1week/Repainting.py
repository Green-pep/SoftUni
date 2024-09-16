nylon_in_sqr = int(input())
paint_in_ltr = int(input())
thinner_in_ltr = int(input())
hours_for_work = int(input())

price_nylon = (nylon_in_sqr + 2) * 1.5
price_paint = (paint_in_ltr + (paint_in_ltr*0.1)) * 14.5
price_thinner = thinner_in_ltr * 5
nylon_bags = 0.40

sum_for_all = price_nylon + price_paint + price_thinner + nylon_bags
sum_for_workers = (sum_for_all * 0.30) * hours_for_work
total_sum = sum_for_all + sum_for_workers

print(total_sum)