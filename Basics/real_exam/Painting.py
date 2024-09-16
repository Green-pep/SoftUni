import math

count_paint_boxes = int(input())
rolls_wallpaper = int(input())
price_gloves = float(input())
price_for_one_brush = float(input())

count_brushes = math.floor(count_paint_boxes * 0.48)
count_gloves = math.ceil(rolls_wallpaper * 0.35)

sum_for_all_boxes = 21.50 * count_paint_boxes
sum_for_all_wallpaper = rolls_wallpaper * 5.20
sum_for_all_brushes = count_brushes * price_for_one_brush
sum_for_all_gloves = count_gloves * price_gloves
sum_all_products = sum_for_all_gloves + sum_for_all_wallpaper + sum_for_all_brushes + sum_for_all_boxes
price_delivery = sum_all_products / 15

print(f"This delivery will cost {price_delivery:.2f} lv.")
