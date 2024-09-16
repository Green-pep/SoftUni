from battle.project import Hotel
from battle.project import Room

room = Room(1, 3)
hotel = Hotel("Nice Hotel")
hotel.add_room(room)
hotel.take_room(1, 3)
hotel.free_room(1)
print(hotel.status())
