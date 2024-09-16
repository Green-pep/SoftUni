quantity_of_decorations = int(input())
days_until_christmas = int(input())

spend_money = 0
christmas_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
points_for_ornament_set = 5
points_for_skirt = 3
points_for_garland = 10
points_for_lights = 17



for days in range(1, days_until_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2

    if days % 2 == 0:
        spend_money += ornament_set_price * quantity_of_decorations
        christmas_spirit += points_for_ornament_set

    if days % 3 == 0:
        spend_money += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        christmas_spirit += points_for_skirt + points_for_garland

    if days % 5 == 0:
        spend_money += tree_lights_price * quantity_of_decorations
        christmas_spirit += points_for_lights
        if days % 3 == 0:
            christmas_spirit += 30

    if days % 10 == 0:
        christmas_spirit -= 20
        spend_money += tree_skirt_price + tree_garland_price + tree_lights_price
if days_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {spend_money}")
print(f"Total spirit: {christmas_spirit}")
