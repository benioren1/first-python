class BankAccount:
    def __init__(self,owner, balance=0,vip = False):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"deposited {amount}.new balance is {self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "not enough mony"



if __name__ == '__main__':
    account1 = BankAccount("beni",-100)
    account2 = BankAccount("david",200)
    account3 = BankAccount("ori")
    account4 = BankAccount("dan",vip = True)
    print(account1.withdraw(1000))
    print(account2.deposit(200))