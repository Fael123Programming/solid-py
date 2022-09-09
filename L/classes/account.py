class Account:

    def __init__(self, owner: str, balance: float):
        self._owner = owner
        self._balance = balance

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self._balance += amount
        return True  # Successful.

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        return True  # Successful.


class CurrentAccount(Account):

    def __init__(self, owner: str, balance: float, withdrawal_fee: float):
        super().__init__(owner, balance)
        self._withdrawal_fee = withdrawal_fee

    def withdraw(self, amount: float) -> bool:
        if super().withdraw(amount):
            # Pay the withdrawal fee if there'S enough money.
            fee = amount * self._withdrawal_fee
            if fee <= self.balance:
                self._balance -= fee
            else:
                self._balance = 0
            return True
        return False


class SavingsAccount(Account):

    def __init__(self, owner: str, balance: float, deposit_benefit_percentage: float):
        super().__init__(owner, balance)
        self._deposit_benefit_percentage = deposit_benefit_percentage

    def deposit(self, amount: float) -> bool:
        if super().deposit(amount):
            self._balance += amount * self._deposit_benefit_percentage
            return True
        return False
