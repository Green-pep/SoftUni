from battle.project import Starter


class Soup(Starter):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name, price, grams: float):
        super().__init__(name, price, grams)
