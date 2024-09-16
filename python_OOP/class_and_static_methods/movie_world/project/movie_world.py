from typing import List

from battle.project import Customer
from battle.project import DVD


class MovieWorld:
    dvd_capacity_of_world = 15
    customer_capacity_of_world = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []


    def dvd_capacity(self):
        return self.dvd_capacity_of_world

    def customer_capacity(self):
        return self.customer_capacity_of_world

    def add_customer(self, customer: Customer):
        if self.customer_capacity_of_world > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity_of_world:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = next((d for d in self.dvds if dvd_id == d.id), None)
        customer = next((c for c in self.customers if customer_id == c.id), None)
        if dvd and customer:
            if dvd.is_rented:
                if dvd.name in customer.rented_dvds:
                    return f"{customer.name} has already rented {dvd.name}"
                return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd.name)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = next((d for d in self.dvds if dvd_id == d.id), None)
        customer = next((c for c in self.customers if customer_id == c.id), None)
        if dvd and customer:
            if dvd.name in customer.rented_dvds:
                customer.rented_dvds.remove(dvd.name)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        list_with_customers_repr = [f"{r.__repr__()}\n" for r in self.customers]
        list_with_dvds_repr = [f"{d.__repr__()}\n" for d in self.dvds]
        return f"{''.join(list_with_customers_repr)}{''.join(list_with_dvds_repr)}"
