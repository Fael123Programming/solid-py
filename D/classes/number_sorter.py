from D.classes.sorting_algorithm import SortingAlgorithm
from datetime import datetime


class NumberSorter:

    def __init__(self, sorting_algorithm: SortingAlgorithm):
        self._sorting_algorithm = sorting_algorithm
        self._time_spent = None

    @property
    def sorting_algorithm(self):
        return self._sorting_algorithm

    @sorting_algorithm.setter
    def sorting_algorithm(self, sorting_algorithm: SortingAlgorithm):
        self._sorting_algorithm = sorting_algorithm

    @property
    def time_spent(self):
        return self._time_spent

    def sort(self, numbers: list):
        start = datetime.now()
        self._sorting_algorithm.sort(numbers)
        self._time_spent = datetime.now() - start
