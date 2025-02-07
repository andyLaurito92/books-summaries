from typing import Protocol, TypeVar
from random import shuffle, choice


class SupportLestThan(Protocol):
    def __lt__(self, other: object) -> bool: ...


Comparable = TypeVar('Comparable', bound=SupportLestThan)
SIZE_LISTS = [3, 5, 10, 15, 17]


def insertionsort(a: list[Comparable]):
    n = len(a)
    for i in range(1, n):
        j = i
        to_insert = a[j]
        while j > 0 and to_insert < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = to_insert


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


def quicksort(a: list[Comparable]):
    def recquicksort(a, low, high):
        if low >= high:
            return
        pivot = a[low]
        i = low + 1
        j = high
        while i < j:
            if a[i] <= pivot:
                i += 1
            elif a[j] > pivot:
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                j -= 1
                i += 1
        a[low], a[j-1] = a[j-1], a[low]

        recquicksort(a, low, i - 1)
        recquicksort(a, i + 1, high)

    shuffle(a)
    recquicksort(a, 0, len(a) - 1)
       

def mergesort(a: list[Comparable]):
    def merge(a, helper, low, med, high):
        for i in range(low, high + 1):
            helper[i] = a[i]

        i = low
        j = med + 1
        for k in range(low, high+1):
            if i > med:
                a[k] = helper[j]
                j += 1
            elif j > high:
                a[k] = helper[i]
                i += 1
            elif helper[j] < helper[i]:
                a[k] = helper[j]
                j += 1
            else:
                a[k] = helper[i]
                i += 1
              
                     
    def sort(a, helper, low, high):
        if (high <= low):
            return
        mid = low + (high - low) // 2
        sort(a, helper, low, mid)
        sort(a, helper, mid+1, high)
        merge(a, helper, low, mid, high)

    helper = [x for x in a]
    sort(a, helper, 0, len(a) - 1)


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
call_sorting_technique(mergesort)

a = [1, 2, 1]
mergesort(a)
