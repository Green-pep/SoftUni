from battle.project import Mammal
from battle.project import Meat, Vegetable, Fruit


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def type_of_eaten_food(self):
        return [Vegetable, Fruit]

    @property
    def take_weight(self):
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def type_of_eaten_food(self):
        return [Meat]

    @property
    def take_weight(self):
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def type_of_eaten_food(self):
        return [Meat, Vegetable]

    @property
    def take_weight(self):
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def type_of_eaten_food(self):
        return [Meat]

    @property
    def take_weight(self):
        return 1
