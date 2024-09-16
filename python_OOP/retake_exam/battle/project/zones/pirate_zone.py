from battle.project.battleships.royal_battleship import RoyalBattleship
from battle.project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code, volume=8):
        super().__init__(code, volume)

    def zone_info(self):
        royal_ships = [ship for ship in self.ships if isinstance(ship, RoyalBattleship)]
        names_of_the_ships = [ship.name for ship in self.get_ships()]
        result = "@Pirate Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += (f"Battleships currently in the Pirate Zone: {len(self.ships)},"
                   f" {len(royal_ships)} out of them are Royal Battleships.\n")
        result += f"#{', '.join(names_of_the_ships)}#"
        return result


