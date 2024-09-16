from battle.project import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price: float, milliliters: float):
        super().__init__(name, price, milliliters)
