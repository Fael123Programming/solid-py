from D.classes.number_sorter import NumberSorter
from D.classes.sorting_algorithm import *

# D for Dependency Inversion Principle.

if __name__ == '__main__':
    quantity = 1000
    n1 = list(i for i in range(quantity, 0, -1))
    n2 = list(i for i in range(quantity, 0, -1))
    n3 = list(i for i in range(quantity, 0, -1))
    print(n1)
    print(n2)
    print(n3)
    print(f'Sorting {quantity} numbers:')
    sorter = NumberSorter(SelectionSort())
    sorter.sort(n1)
    print(n1)
    print(f'Selection Sort: {sorter.time_spent}')
    sorter.sorting_algorithm = BubbleSort()
    sorter.sort(n2)
    print(n2)
    print(f'Bubble Sort: {sorter.time_spent}')
    sorter.sorting_algorithm = InsertionSort()
    sorter.sort(n3)
    print(n3)
    print(f'Insertion Sort: {sorter.time_spent}')
