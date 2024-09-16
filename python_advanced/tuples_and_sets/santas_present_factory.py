from collections import deque


materials_for_crafting = [int(x) for x in input()]
magic_level = deque(int(x) for x in input())

magic_table = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

