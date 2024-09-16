from abc import ABC, abstractmethod
from typing import List, Type
from battle.project import Food


class Animal(ABC):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def type_of_eaten_food(self) -> List[Type[Food]]:
        pass

    @property
    @abstractmethod
    def take_weight(self) -> float:
        pass

    def feed(self, food: Food):
        if type(food) not in self.type_of_eaten_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.take_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: int, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"