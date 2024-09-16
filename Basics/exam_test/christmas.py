wrapping_paper = int(input())
rolls_cloth = int(input())
liters_glue = float(input())
discount_percentages = int(input())

price_for_all_paper = 5.80 * wrapping_paper
price_for_all_plat = 7.20 * rolls_cloth
price_for_all_glue = 1.20 * liters_glue

sum_for_all = price_for_all_glue + price_for_all_plat + price_for_all_paper
sum_with_discount = sum_for_all - ((sum_for_all * discount_percentages) / 100)

print(f"{sum_with_discount:.3f}")
