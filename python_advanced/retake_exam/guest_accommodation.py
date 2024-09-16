from collections import deque


def accommodate(*waiting_guests, **available_rooms):
    taken_rooms = {}
    guest_queue = deque(waiting_guests)
    sorted_rooms = sorted(available_rooms.items(), key=lambda item: (item[1], item[0]))
    room_tries = 0
    while guest_queue and sorted_rooms:
        current_guests = guest_queue.popleft()

        for room, capacity in sorted_rooms:
            if capacity >= current_guests:
                taken_rooms[room[5:]] = current_guests
                sorted_rooms.remove((room, capacity))
                break
        else:
            room_tries += 1
            if room_tries > len(guest_queue):
                guest_queue.append(current_guests)
                break
            guest_queue.append(current_guests)
            continue

    sorted_taken_rooms = sorted(taken_rooms.items(), key=lambda item: int(item[0]))

    if sorted_taken_rooms:
        result = f"A total of {len(sorted_taken_rooms)} accommodations were completed!\n"
        for room, capacity in sorted_taken_rooms:
            result += f"<Room {room} accommodates {capacity} guests>\n"
    else:
        result = "No accommodations were completed!\n"
    free_rooms = [room[5:] for room in available_rooms if room[5:] not in taken_rooms]
    if guest_queue:
        result += f"Guests with no accommodation: {sum(guest_queue)}\n"
    if free_rooms:
        result += f"Empty rooms: {len(free_rooms)}\n"
    return result



# print(accommodate(5, 4, 2, 6, room_305=6, room_410=5, room_204=2))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))