from abc import ABC, abstractmethod
from typing import List
from battle.project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code, volume):
        self.code = code
        self.volume = volume
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self._code = value

    def get_ships(self):
        sorted_ships = sorted(
            self.ships, key=lambda ship: (-ship.hit_strength, ship.name)
        )
        return sorted_ships

    @abstractmethod
    def zone_info(self):
        """Keep in mind that each type of zone implements the method differently."""
        pass