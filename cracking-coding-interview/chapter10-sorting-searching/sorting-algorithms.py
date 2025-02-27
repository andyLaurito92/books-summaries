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


"""
Note: This quicksort doesn't perform that well in the
presence of duplicates. Why? Because when we have elements
that equal the pivot element, it would be nice to already
ordered those elements in the place they have to be. Which is
this place? The same one than the pivot!

In this implementation, duplicate elements are just moved to
one part of the subarray (in this particular implementation, to
the left part), and are NOT NECESSARILY IN ORDER.
Ex: [5, 1, 1, 3, 5, 8, 5, 4, 3, 2, 1]

Grab the above list as example: If we pick pivot 5, then we have after the
first run:
[1, 1, 3, 5, 1, 5, 4, 3, 2, 1, 5, 8]

Remember that quicksort is an stable algorithm, so the relative order of the
5th elements didn't change, however, they r still not in their final position.

3-way quicksort handles this problem by having another idx for managing duplicates
"""

# [3, 2, 1, 3, 1], i = 0, j = 4, pivot = 3
# [3, 2, 1, 3, 1], i = 1, j = 4, pivot = 3
# [3, 2, 1, 3, 1], i = 2, j = 4, pivot = 3
# [3, 2, 1, 3, 1], i = 3, j = 4, pivot = 3
# [3, 2, 1, 3, 1], i = 4, j = 4, pivot = 3
# [1, 2, 1, 3, 3], i = 5, j = 4, pivot = 3

# [1, 2, 1, 3, 3], i = 0, j = 4, pivot = 1
def quicksort(a: list[Comparable]):
    def recquicksort(a, low, high):
        if low >= high:
            return
        pivot = a[low]
        i = low
        j = high
        while i <= j:
            while i <= j and a[i] <= pivot:
                i += 1
            while i <= j and a[j] > pivot:
                j -= 1
            if i > j:
                break
            a[i], a[j] = a[j], a[i]
        a[low], a[j] = a[j], a[low]

        recquicksort(a, low, j - 1)
        recquicksort(a, j + 1, high)

    shuffle(a)
    recquicksort(a, 0, len(a) - 1)

def threewayquicksort(a: list[Comparable]):
    def recquicksort(a: list[Comparable], i: int, j: int) -> None:
        if i >= j:
            return
        pivot = a[i]
        lt = i
        k = lt
        gt = j
        while k <= gt:
            if a[k] > pivot:
                a[gt], a[k] = a[k], a[gt]
                gt -= 1
            elif a[k] < pivot:
                a[lt], a[k] = a[k], a[lt]
                lt += 1
                k += 1
            else: # a[lt] == pivot
                k += 1

        recquicksort(a, i, lt - 1)
        recquicksort(a, gt + 1, j) 

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
call_sorting_technique(quicksort)
call_sorting_technique(threewayquicksort)

a = [1, 2, 1]
mergesort(a)
