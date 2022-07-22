class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount1(int_rate = 0.02, balance = 0)
        self.account2 = BankAccount2(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount, account):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount, account):
        if(self.account.balance - amount) >= 0:
            self.account.balance -= amount
        else:
            self.account.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_user_balance(self, account):
        print(self.account.balance)
        return self

    def transfer_money(self, amount, account, other_user):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

class User2:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount1(int_rate = 0.02, balance = 50)
        self.account2 = BankAccount2(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount, account):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount, account):
        if(self.account.balance - amount) >= 0:
            self.account.balance -= amount
        else:
            self.account.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_user_balance(self, account):
        print(self.account.balance)
        return self

    def transfer_money(self, amount, account, other_user):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

class BankAccount1:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount1.accounts.append(self)

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

class BankAccount2:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount2.accounts.append(self)

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

nathan = User("Nathan", "123@email.com")

lyndsay = User2("Lyndsay", "321@superemail.com")


nathan.display_user_balance(BankAccount1).make_deposit(100, BankAccount1).make_withdrawal(50, BankAccount1).display_user_balance(BankAccount1)

nathan.display_user_balance(BankAccount2).make_deposit(100, BankAccount2).make_withdrawal(50, BankAccount2).transfer_money(50, BankAccount2, lyndsay).display_user_balance(BankAccount2)

lyndsay.display_user_balance(BankAccount2)