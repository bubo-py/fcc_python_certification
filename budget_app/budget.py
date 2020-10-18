
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.dictionary = {"amount": amount, "description": description}
        self.ledger.append(self.dictionary)

    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.dictionary = {"amount": amount * -1, "description": description}
        if self.check_funds(amount):
            self.ledger.append(self.dictionary)
            return True
        else:
            return False

    def get_balance(self):
        self.balance = list()
        for values in self.ledger:
            self.balance.append(values.get('amount'))
        return sum(self.balance)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        printed = self.category.center(30, '*') + '\n'
        formated_description = lambda item : item['description'][:23].ljust(23)
        formated_amount = lambda item : format(item['amount'], '.2f').rjust(7)

        for item in self.ledger:
            printed += f"{formated_description(item)}{formated_amount(item)}\n"

        printed += f"Total: {format(self.get_balance(), '.2f')}" # '.2f' is code for number formating in python
        return printed


def create_spend_chart(categories):
    pass # todo
