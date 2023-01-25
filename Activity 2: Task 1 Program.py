import banking
calc = banking.SavingAccount()
calc.deposit(1000)
print(calc.check_balance())

fixed = banking.FixedDeposit()
fixed.open_fixed_deposit(2000)
print(fixed.calculate_maturity_amount())
