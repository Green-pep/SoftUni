from collections import deque
client_as_deque = deque([])

while True:
    client = input()

    if client == "End":
        break

    # Loop for Paid queue. Continue is to not append Paid command to the deque.
    elif client == "Paid":
        while client_as_deque:
            print(client_as_deque.popleft())
        continue

    client_as_deque.append(client)

print(f"{len(client_as_deque)} people remaining.")
