from battle.project import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return "Meow"
