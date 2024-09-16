def dungeon(command_text, health, bitcoin):
    command_text = command_text.split("|")
    is_died = False
    best_room = 0

    for command in command_text:
        best_room += 1
        split_command = command.split()
        room = split_command[0]
        value = int(split_command[1])
        if room == "potion":
            health += value
            if health > 100:
                additional_health = abs(abs(100 - health) - value)
                health = 100
                value = additional_health
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")
        elif room == "chest":
            bitcoin += value
            print(f"You found {value} bitcoins.")
        else:
            health -= value
            monster = room
            if health <= 0:
                print(f"You died! Killed by {monster}.")
                print(f"Best room: {best_room}")
                is_died = True
                break
            else:
                print(f"You slayed {monster}.")

    if not is_died:
        print("You've made it!")
        print(f"Bitcoins: {bitcoin}")
        print(f"Health: {health}")


command_line = input()
health_hero = 100
bitcoins = 0
dungeon(command_line, health_hero, bitcoins)
