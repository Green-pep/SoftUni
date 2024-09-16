from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking: bool = False
        self.is_available: bool = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self._name = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    def take_damage(self, enemy_battleship):
        self.health -= enemy_battleship.hit_strength

    @abstractmethod
    def attack(self):
        """Each type of battleship implements this method differently."""
        pass