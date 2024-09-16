from typing import List

from battle.project import Animal
from battle.project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price) -> str:
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        is_exist_name = next((el for el in self.workers if worker_name == el.name), False)
        if is_exist_name:
            self.workers.remove(is_exist_name)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salary = sum(w.salary for w in self.workers)
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animals_money_for_care = [a.money_for_care for a in self.animals]
        if sum(total_animals_money_for_care) <= self.__budget:
            self.__budget -= sum(total_animals_money_for_care)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        total_lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        total_tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        total_cheetah = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        return (
                f"You have {len(self.animals)} animals" + "\n" +
                f'----- {len(total_lions)} Lions:\n' +
                "\n".join([repr(a) for a in total_lions]) + "\n" +
                f'----- {len(total_tigers)} Tigers:\n' +
                "\n".join([repr(a) for a in total_tigers]) + "\n" +
                f'----- {len(total_cheetah)} Cheetahs:\n' +
                "\n".join([repr(a) for a in total_cheetah])
        )

    def workers_status(self):
        total_keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        total_caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        total_vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        return (
                f"You have {len(self.workers)} workers" + "\n" +
                f'----- {len(total_keepers)} Keepers:\n' +
                "\n".join([repr(w) for w in total_keepers]) + "\n" +
                f'----- {len(total_caretakers)} Caretakers:\n' +
                "\n".join([repr(w) for w in total_caretakers]) + "\n" +
                f'----- {len(total_vets)} Vets:\n' +
                "\n".join([repr(w) for w in total_vets])
        )








