quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_gerland_price = 3
tree_lights_price = 15
cost_counter = 0
spirit_counter = 0


for days_for_shopping in range(1, days_left_until_christmas + 1):
    if days_for_shopping % 11 == 0:
        quantity_of_decorations += 2

    if days_for_shopping % 2 == 0:
        cost_counter += ornament_set_price * quantity_of_decorations
        spirit_counter += 5

    if days_for_shopping % 3 == 0:
        cost_counter += (tree_skirt_price + tree_gerland_price) * quantity_of_decorations
        spirit_counter += 13

    if days_for_shopping % 5 == 0:
        cost_counter += tree_lights_price * quantity_of_decorations
        spirit_counter += 17
        if days_for_shopping % 3 == 0:
            spirit_counter += 30

    if days_for_shopping % 10 == 0:
        spirit_counter -= 20
        cost_counter += tree_skirt_price + tree_gerland_price + tree_lights_price

if days_left_until_christmas % 10 == 0:
    spirit_counter -= 30
print(f"Total cost: {cost_counter}")
print(f"Total spirit: {spirit_counter}")
