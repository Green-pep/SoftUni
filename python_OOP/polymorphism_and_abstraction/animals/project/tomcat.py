from battle.project import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"
    