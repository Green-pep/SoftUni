from battle.project import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model: str, price: float):
        super().__init__(model, price, material='Wood/Plastic', sub_type='Toys')

    def discount(self):
        discount = self.price * 0.2
        return self.price - discount
