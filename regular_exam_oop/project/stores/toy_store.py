from battle.project import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    @property
    def store_type(self):
        type_of_store = "ToyStore"
        return type_of_store

    def store_stats(self):

        pass
