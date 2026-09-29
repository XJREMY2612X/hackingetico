# 1. Clase BankAccount[cite: 10]
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Error: Fondos insuficientes para evitar saldo negativo.")
