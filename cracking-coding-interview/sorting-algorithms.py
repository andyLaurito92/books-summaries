from typing import Protocol, TypeVar
from random import shuffle, choice


class SupportLestThan(Protocol):
    def __lt__(self, other: object) -> bool: ...


Comparable = TypeVar('Comparable', bound=SupportLestThan)
SIZE_LISTS = {10, 15, 17}


def insertionsort(a: list[Comparable]):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def bubblesort(a: list[Comparable]):
    n = len(a)
    # 1, 5, 3, 4, 2
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break


def selectionsort(a: list[Comparable]):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


def log(message):
    print(message)


def call_sorting_technique(algorithm):
    for n in SIZE_LISTS:
        size = range(n)
        a = [choice(size) for _ in size]
        shuffle(a)

        log(f"Starting {algorithm.__name__} with list {a}")
        algorithm(a)
        log(f"{algorithm.__name__} output: {a}")
        log("\n")


call_sorting_technique(bubblesort)
call_sorting_technique(selectionsort)
call_sorting_technique(insertionsort)
