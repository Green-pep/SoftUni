packages_pens = int(input())
packages_markers = int(input())
desk_cleaner_ltr = int(input())
disscount = int(input())

price_pens = packages_pens * 5.80
price_markers = packages_markers * 7.20
price_cleaner = desk_cleaner_ltr * 1.20

sum_for_all = price_pens + price_markers + price_cleaner
final_sum = sum_for_all - (sum_for_all * (disscount/100))

print(final_sum)
