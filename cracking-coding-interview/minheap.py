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
