from battle.project import Food


class Dessert(Food):

    def __init__(self, name, price, grams: float, calories: float):
        super().__init__(name, price, grams)
        self.__calories = calories
