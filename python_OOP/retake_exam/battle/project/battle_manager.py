from typing import List

from battle.project.battleships.base_battleship import BaseBattleship
from battle.project.battleships import PirateBattleship
from battle.project.battleships.royal_battleship import RoyalBattleship
from battle.project.zones.base_zone import BaseZone
from battle.project.zones.pirate_zone import PirateZone
from battle.project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        is_zone_code_exist = any(z for z in self.zones if zone_code == z.code)
        if is_zone_code_exist:
            raise Exception(f"Zone already exists!")

        if zone_type == "RoyalZone":
            self.zones.append(RoyalZone(zone_code))
        elif zone_type == "PirateZone":
            self.zones.append(PirateZone(zone_code))
        else:
            raise Exception(f"Invalid zone type!")

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type == "PirateBattleship":
            self.ships.append(PirateBattleship(name, health, hit_strength))
        elif ship_type == "RoyalBattleship":
            self.ships.append(RoyalBattleship(name, health, hit_strength))
        else:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume < 1:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if isinstance(ship, RoyalBattleship) and isinstance(zone, RoyalZone):
            ship.is_attacking = True
        elif isinstance(ship, PirateBattleship) and isinstance(zone, PirateZone):
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if not ship:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."
    def start_battle(self, zone: BaseZone):
        attackers = [ship for ship in zone.ships if ship.is_attacking]
        defenders = [ship for ship in zone.ships if not ship.is_attacking]
        if len(attackers) < 1 or len(defenders) < 1:
            return f"Not enough participants. The battle is canceled."

        attacker_with_the_most_hit_attack = max(attackers, key=lambda x: x.hit_strength, default=None)
        defender_with_the_most_health = max(defenders, key=lambda x: x.health, default=None)

        attacker_with_the_most_hit_attack.attack()
        defender_with_the_most_health.take_damage(attacker_with_the_most_hit_attack)

        if defender_with_the_most_health.health == 0:
            zone.ships.remove(defender_with_the_most_health)
            zone.volume += 1
            return f"{defender_with_the_most_health.name} lost the battle and was sunk."

        if attacker_with_the_most_hit_attack.ammunition == 0:
            zone.ships.remove(attacker_with_the_most_hit_attack)
            zone.volume += 1
            return f"{attacker_with_the_most_hit_attack.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available == True]
        if available_ships:
            available_names = [s.name for s in available_ships]
            print(f"Available Battleships: {len(available_ships)}\n#{', '.join(available_names)}#")

        result = "***Zones Statistics:***\n"
        for zone in self.zones:
            result += zone.zone_info()

        return result