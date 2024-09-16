from battle.project import Bird
from battle.project import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def type_of_eaten_food(self):
        return [Meat]

    @property
    def take_weight(self):
        return 0.25


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def type_of_eaten_food(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def take_weight(self):
        return 0.35



