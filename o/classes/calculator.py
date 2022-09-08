from o.classes.operation import Operation


class Calculator:

    def __init__(self, operation: Operation):
        self._operation = operation

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation: Operation):
        self._operation = operation

    def calculate(self, x: float | int, y: float | int):
        return self._operation.calculate(x, y)

