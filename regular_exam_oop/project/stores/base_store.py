import statistics
from abc import ABC, abstractmethod
from typing import List


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int = 0):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if len(value) != 3 or " " in value:
            raise ValueError(
                "Store location must be 3 chars long and have no white spaces"
            )
        self._location = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self._capacity = value

    def get_estimated_profit(self):
        price_of_products = sum([product.price for product in self.products])
        estimated_profit = price_of_products * 0.1
        products_count = len(self.products)
        return f"Estimated future profit for {products_count} products is {estimated_profit}"

    @property
    def store_type(self):
        """This method will be implemented differently for every inheritance class"""
        type_of_store = ""
        return type_of_store


    def store_stats(self):
        dict_with_products = {}
        for product in self.products:
            if product.model not in dict_with_products:
                dict_with_products[product.model] = []
            dict_with_products[product.model].append(product.price)
        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += f"{self.get_estimated_profit()}\n"
        result += "**Furniture for sale:\n"
        for model, prices in sorted(dict_with_products.items()):
            count_of_products = len(prices)
            average_price_of_model = statistics.mean(prices)
            result += f"{model}: {count_of_products}pcs, average price: {average_price_of_model:.2f}\n"
        return result

