class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, "r") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposite(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount - self.fee

checking = Checking("balance.txt", 1)   
checking.deposite(200)
checking.commit()
checking.transfer(10)
checking.commit()
print(checking.balance)

# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# account.deposite(3000)
# account.commit()
# print(account.balance)
