from battle.project import Dessert


class Cake(Dessert):
    def __init__(self, name, food, price, grams: float, calories: float):
        super().__init__(name, price, grams, calories)