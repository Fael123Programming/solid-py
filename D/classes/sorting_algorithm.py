from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):

    @abstractmethod
    def sort(self, numbers: list):
        pass


class SelectionSort(SortingAlgorithm):

    def sort(self, numbers: list):
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


class BubbleSort(SortingAlgorithm):

    def sort(self, numbers: list):
        n = len(numbers)
        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    swapped = True
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            if not swapped:
                return


class InsertionSort(SortingAlgorithm):

    def sort(self, numbers: list):
        for j in range(1, len(numbers)):
            value = numbers[j]
            i = j - 1
            while i >= 0 and numbers[i] > value:
                numbers[i + 1] = numbers[i]
                i -= 1
            numbers[i + 1] = value


