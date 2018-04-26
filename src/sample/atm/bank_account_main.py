from bank_account import BankAccount

joes_account = BankAccount(500)

print(joes_account.get_balance())
print()
joes_account.deposit(500)

print(joes_account.get_balance())

print()
joes_account.withdraw(100)


print(joes_account.get_balance())
