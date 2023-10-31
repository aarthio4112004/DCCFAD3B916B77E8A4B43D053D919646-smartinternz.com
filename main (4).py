class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")

# Example usage of the BankAccount class
if __name__ == "__main__":
    account1 = BankAccount("John Doe", 1000)
    account1.display_account_info()
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_account_info()