from o.classes.calculator import Calculator
from o.classes.operation import Sum, Subtraction

# O for Open-Closed Principle

if __name__ == '__main__':
    c = Calculator(Sum())
    print(c.calculate(78, 22))
    c.operation = Subtraction()
    print(c.calculate(100, 22))
