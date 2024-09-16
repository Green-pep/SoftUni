guests = int(input())

guest_list = set()

for _ in range(guests):
    guest = input()
    guest_list.add(guest)

while True:
    welcome_peoples = input()
    if welcome_peoples == "END":
        break
    if welcome_peoples in guest_list:
        guest_list.remove(welcome_peoples)

print(len(guest_list))

sorted_guests = sorted(guest_list)

for res in sorted_guests:
    print(res)

