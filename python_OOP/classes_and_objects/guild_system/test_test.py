import self
from battle.project import Player

player = Player("Pesho", 90, 90)
player.add_skill("A", 3)
print(player.player_info())
