from typing import List

from battle.project import Customer
from battle.project import Equipment
from battle.project import ExercisePlan
from battle.project import Subscription
from battle.project import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subs_id = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer_result = next((c for c in self.customers if c.id == subs_id.customer_id), None)
        trainer_result = next((t for t in self.trainers if t.id == subs_id.trainer_id), None)
        equipment_result = next((e for e in self.equipment if e.id == subs_id.exercise_id), None)
        plan_result = next((p for p in self.plans if p.id == subs_id.exercise_id), None)
        return '\n'.join([subs_id.__repr__(),
                          customer_result.__repr__(),
                          trainer_result.__repr__(),
                          equipment_result.__repr__(),
                          plan_result.__repr__()])

