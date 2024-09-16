from collections import deque

materials_for_crafting_toys = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

table_with_presents = {150: "Doll",
                       250: "Wooden train",
                       300: "Teddy bear",
                       400: "Bicycle"
                       }
crafted_presents = {}
is_succeeded = False

while materials_for_crafting_toys and magic_level:
    product_number = materials_for_crafting_toys[-1] * magic_level[0]

    if product_number in table_with_presents:
        product_number = materials_for_crafting_toys.pop() * magic_level.popleft()
        new_present = table_with_presents[product_number]

        if new_present in crafted_presents:
            crafted_presents[new_present] += 1
        else:
            crafted_presents[new_present] = 1

    elif product_number < 0:
        product_number = materials_for_crafting_toys.pop() + magic_level.popleft()
        materials_for_crafting_toys.append(product_number)

    elif product_number not in table_with_presents and product_number > 0:
        magic_level.popleft()
        materials_for_crafting_toys[-1] += 15
    else:
        if materials_for_crafting_toys[-1] == 0:
            materials_for_crafting_toys.pop()
        elif magic_level[0] == 0:
            magic_level.popleft()

if crafted_presents.get("Doll") and crafted_presents.get("Wooden train"):
    is_succeeded = True
elif crafted_presents.get("Teddy bear") and crafted_presents.get("Bicycle"):
    is_succeeded = True

print("The presents are crafted! Merry Christmas!" if is_succeeded else "No presents this Christmas!")

if materials_for_crafting_toys:
    print("Materials left:", ", ".join(map(str, reversed(materials_for_crafting_toys))))
if magic_level:
    print("Magic left:", ", ".join(map(str, magic_level)))

for key, value in sorted(crafted_presents.items()):
    print(f"{key}: {value}")
