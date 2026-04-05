#Bank Account System#
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Balance:", self.balance)

b = BankAccount(101, 1000)
b.deposit(500)
b.withdraw(200)
b.display()