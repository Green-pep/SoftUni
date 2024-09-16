from battle.project.battleships import PirateBattleship
from battle.project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code, volume=10):
        super().__init__(code, volume)

    def zone_info(self):
        pirate_ships = [ship for ship in self.ships if isinstance(ship, PirateBattleship)]
        names_of_the_ships = [ship.name for ship in self.get_ships()]
        result = "@Royal Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += (f"Battleships currently in the Royal Zone: {len(self.ships)},"
                   f" {len(pirate_ships)} out of them are Pirate Battleships.\n")
        result += f"#{', '.join(names_of_the_ships)}#"
        return result


