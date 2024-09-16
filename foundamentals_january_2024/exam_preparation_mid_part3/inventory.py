items = input().split(", ")

while True:
    text = input()
    if text == "Craft!":
        break
    new_text = text.split(" - ")
    command = new_text[0]
    new_item = new_text[1]
    if command == "Collect":
        if new_item not in items:
            items.append(new_item)
    elif command == "Drop":
        if new_item not in items:
            continue
        items.remove(new_item)
    elif command == "Combine Items":
        new_item = new_item.split(":")
        old_items = new_item[0]
        new_items = new_item[1]
        if old_items not in items:
            continue

        item_index = items.index(old_items)
        items.insert(item_index + 1, new_items)
    elif command == "Renew":
        if new_item not in items:
            continue
        items.remove(new_item)
        items.append(new_item)
print(", ".join(items))
