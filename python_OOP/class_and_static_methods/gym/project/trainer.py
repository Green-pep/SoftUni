from battle.project import IDMixin


class Trainer(IDMixin):
    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.new_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"


