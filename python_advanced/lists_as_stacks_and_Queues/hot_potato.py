from collections import deque

players = deque(input().split())
tosses = int(input())
while True:
    if len(players) == 1:
        break
    for toss in range(tosses - 1):
        first_player = players.popleft()
        players.append(first_player)
    print(f"Removed {players.popleft()}")
print(f"Last is {players.popleft()}")