from banking import *
calc = SavingAccount()
calc.deposit(1000)
print(calc.check_balance())

fixed = FixedDeposit()
fixed.open_fixed_deposit(2000)
print(fixed.calculate_maturity_amount())
