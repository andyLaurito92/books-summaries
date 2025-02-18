class MinHeap:
    def __init__(self):
        self.pq = [None]
        self.n = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def insert(self, v) -> None:
        self.n += 1
        self.pq.append(v)
        self._swim(self.n)

    def _swim(self, k: int) -> None:
        while (k > 1 and self.pq[k//2] > self.pq[k]):
            self.pq[k//2], self.pq[k] = self.pq[k], self.pq[k//2]
            k = k//2

    def _sink(self, k: int) -> None:
        while (2*k <= self.n):
            j = 2*k
            if (j < self.n and self.pq[j] >= self.pq[j+1]):
                j += 1

            if self.pq[k] < self.pq[j]:
                break

            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j
              
    def delmax(self) -> int:
        max = self.pq[1]
        self.pq[1] = self.pq[self.n]
        del self.pq[self.n]
        self.n -= 1
        self._sink(1)
        return max


elements = [1, 3, -3, -10, 8, 22, 0, 12]

myheap = MinHeap()
for el in elements:
    myheap.insert(el)
    

"""
We can also use Python heapq implementation
https://docs.python.org/3/library/heapq.html
"""

from heapq import heapify, heappush, heappop

heapify(elements) # transforms the list into a heap in linear 
