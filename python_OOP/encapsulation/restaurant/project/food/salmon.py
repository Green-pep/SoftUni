from battle.project import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price, grams: float):
        super().__init__(name, price, grams)