class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def transaction_checker(
        transaction_amount: int, balance: int, all_transactions: list
    ):
        if (sum(all_transactions) + transaction_amount) < 0:
            raise ValueError(f"sorry cannot go in debt!")
        all_transactions.append(transaction_amount)
        return f"New balance: {balance + sum(all_transactions)}", all_transactions

    def handle_transaction(self, transaction_amount):
        result, self._transactions = self.transaction_checker(
            transaction_amount, self.balance, self._transactions
        )
        return result

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError(f"please use int for amount")
        result, self._transactions = self.transaction_checker(
            amount, self.balance, self._transactions
        )
        return result

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other: "Account"):
        new_class = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_class._transactions = self._transactions + other._transactions
        return new_class


acc = Account("bob", 10)
acc2 = Account("john")
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
