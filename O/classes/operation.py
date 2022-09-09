from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def calculate(self, x: float | int, y: float | int) -> float | int:
        pass


class Sum(Operation):

    def calculate(self, x: float | int, y: float | int) -> float | int:
        return x + y


class Subtraction(Operation):

    def calculate(self, x: float | int, y: float | int) -> float | int:
        return x - y


# If you want to add another operation, it is just a matter of creating a new class
# that inherits from Operation and implements the calculate method.
