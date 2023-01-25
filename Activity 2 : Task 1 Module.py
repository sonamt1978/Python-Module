class SavingAccount:
    def __init__(self, bal=0):
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        self.bal -= amount

    def check_balance(self):
        return self.bal
        
class FixedDeposit:
    def __init__(self, rate=0.07, term=12):
        self.rate = rate
        self.term = term

    def open_fixed_deposit(self, amount):
        self.amount = amount

    def calculate_maturity_amount(self):
        return self.amount+(self.amount*self.rate*self.term)/12

    def close_fixed_deposit(self):
        self.amount = 0
