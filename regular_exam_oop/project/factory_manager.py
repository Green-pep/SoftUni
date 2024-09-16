from typing import List

from battle.project import BaseProduct
from battle.project import Chair
from battle.project import HobbyHorse
from battle.project import BaseStore
from battle.project import FurnitureStore
from battle.project import ToyStore


class FactoryManager:
    def __init__(self, name: str, income: float = 0.0):
        self.name = name
        self.income = income
        self.products: List = []
        self.stores: List = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            new_product = Chair(model, price)
        elif product_type == "HobbyHorse":
            new_product = HobbyHorse(model, price)
        else:
            return "Invalid product type!"

        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type == "FurnitureStore":
            new_store = FurnitureStore(name, location)
        elif store_type == "ToyStore":
            new_store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if not store.capacity >= len(products):
            return f"Store {store.name} has no capacity for this purchase."

        product_type = {"FurnitureStore": "Furniture", "ToyStore": "Toys"}
        filtered_products = [product for product in products if product.sub_type == product_type[store.store_type]]
        if not filtered_products:
            return "Products do not match in type. Nothing sold."
        store.products.extend(filtered_products)
        store.products = [product for product in self.products if product not in filtered_products]
        store.capacity -= len(filtered_products)
        price_of_products = sum(product.price for product in filtered_products)
        self.income += price_of_products
        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store_name = next((store for store in self.stores if store.name == store_name), None)
        if not store_name:
            raise Exception("No such store!")
        if store_name.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store_name)
        return f"Successfully unregistered store {store_name.name}, location: {store_name.location}."

    def discount_products(self, product_model: str):
        products_for_discount = [product for product in self.products if product.model == product_model]
        for product in products_for_discount:
            product.discount()
        return f"Discount applied to {len(products_for_discount)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((store for store in self.stores if store.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        product_stats = {}
        for product in self.products:
            if product.model not in product_stats:
                product_stats[product.model] = 0
            product_stats[product.model] += 1
        products_sorted = sorted(product_stats.items())
        products_price = sum(p.price for p in self.products)
        store_names = sorted(store.name for store in self.stores)
        total_stores_count = len(self.stores)
        result = f"Factory: {self.name}\nIncome: {self.income:.2f}\n"
        result += "***Products Statistics***\n"
        result += f"Unsold Products: {len(self.products)}. Total net price: {products_price:.2f}\n"
        for model, count in products_sorted:
            result += f"{model}: {count}\n"
        result += f"***Partner Stores: {total_stores_count}***\n"
        for store_name in store_names:
            result += f"{store_name}\n"
        return result
