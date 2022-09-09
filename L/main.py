from L.classes.account import *


# L for Liskov Substitution Principle.

def deposit_in_account(account: Account, amount: float):
    former_balance = account.balance
    if account.deposit(amount):
        print(f'Former balance: ${former_balance}\nDeposited ${amount}\nCurrent balance: ${account.balance}')
    else:
        print('Something went wrong when trying to deposit to the account.')
    print('-' * 150)


def withdraw_from_account(account: Account, amount: float):
    former_balance = account.balance
    if account.withdraw(amount):
        print(f'Former balance: ${former_balance}\nWithdrawn ${amount}\nCurrent balance: ${account.balance}')
    else:
        print('Something went wrong when trying to withdraw from the account.')
    print('-' * 150)


if __name__ == '__main__':
    c1 = Account('Matthew', 500)
    deposit_in_account(c1, 500)
    c2 = CurrentAccount('Josh', 1000, 0.01)  # 1% of fee.
    withdraw_from_account(c2, 500)
    c3 = SavingsAccount('Rafael', 200, 0.02)  # 2% of benefit.
    deposit_in_account(c3, 800)
