class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit must be greater than 0")
        self.balance += amount
        print(f"✅ Deposit of {amount}. Your actual balance is: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdraw must be greater than 0")
        if amount > self.balance:
            raise ValueError("❌ Insufficient funds")
        self.balance -= amount
        print(f"✅ Withdraw of {amount}. Your actual balance: {self.balance}")


class SavingsAccount(Bank):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdraw must be greater than 0")
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"❌ Error. You cannot withdraw {amount}. "
                f"The balance cannot be less than {self.min_balance}"
            )
        self.balance -= amount
        print(f"✅ Withdraw of {amount}. Your actual balance: {self.balance}")



account = SavingsAccount(balance=500, min_balance=100)
account.deposit(1000)   
account.withdraw(600)   
account.withdraw(500)   
