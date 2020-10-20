
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

    # set initial values
    longest_name = 0
    w = 0
    withdrawls = []
    rounded_to_ten = lambda n : 0 if n < 10 else round(n / 10.0) * 10 # function to round number to nearest 10
  
    # loop through given categories
    for item in categories:
        w_amount = 0 # total value of withdrawals

        # loop through ledgers of categories
        for l in item.ledger:
            # check for withdrawals
            if l["amount"] < 0: # get only withdrawals
                w_amount += l["amount"]
                w += l["amount"]
        
        # get the longest category name (needed for later)
        if len(item.category) > longest_name:
            longest_name = len(item.category)

        # add values to list of withdrawls
        withdrawls.append([item.category, w_amount])

    # get % of the category
    for p in withdrawls:
        p.append(rounded_to_ten((p[1] / w) * 100))

    # more initial values
    output = "Percentage spent by category\n"
    top = 100

    # continue following steps until percentage is 0 (chart from up to down)
    while top >= 0:
        # add numbers and vertical bars to the output
        output += str(top).rjust(3) + "|" + " "

        # adding 'o' characters in the chart
        for n in range(len(withdrawls)):
            if withdrawls[n][2] >= top:
                output += "o" + "  "
            else:
                output += "   "

        # every loop decrease value of 'top' (chart from up to down)
        top -= 10
        output += "\n" # let every iteration start from new line

    # adding 'finisher' to the bottom
    output += "    " + ("-" * 10) + "\n"

    c = 0
    for n in range(longest_name):
        output += "     "
        for j in range(len(withdrawls)):
            # check for length of the category
            if len(withdrawls[j][0]) -1 < c:
                # add space if no character
                output += "   "
            else:
                # add character in correct line
                output += withdrawls[j][0][c] + "  "
        c += 1
        # add newline
        if n != longest_name - 1:
            output += "\n"

    return output
