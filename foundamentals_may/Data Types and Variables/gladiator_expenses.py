lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_breaks = lost_fights_count // 2
sword_breaks = lost_fights_count // 3
shield_breaks = lost_fights_count // 6
armor_breaks = shield_breaks // 2

price_for_equipment = helmet_price * helmet_breaks \
    + sword_price * sword_breaks \
    + shield_price * shield_breaks \
    + armor_price * armor_breaks

print(f"Gladiator expenses: {price_for_equipment:.2f} aureus")