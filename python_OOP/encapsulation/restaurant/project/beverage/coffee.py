from battle.project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)