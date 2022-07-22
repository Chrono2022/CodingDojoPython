class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def display_all(cls):
        for account in cls.accounts:
            account.display_account_info()

nathansAccount = BankAccount(.2, 100)

lyndsaysAccount = BankAccount(.1, 500)

nathansAccount.deposit(5).deposit(10).deposit(15).withdraw(5).yield_interest().display_account_info()

lyndsaysAccount.deposit(100).deposit(200).withdraw(100).withdraw(200).withdraw(80).withdraw(1000).display_account_info()

BankAccount.display_all()