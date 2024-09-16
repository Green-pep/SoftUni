from typing import List

from battle.project import Chair
from battle.project import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)
        self.products: List[Chair] = []

    @property
    def store_type(self):
        type_of_store = "FurnitureStore"
        return type_of_store

