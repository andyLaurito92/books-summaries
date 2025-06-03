
def run_length_encoding(mystr: str) -> bytearray:
    """
    Encodes the received string using the run length encoding
    """
    return []

    
from collections import Counter
import heapq

class TrieNode:
    def __init__(self, char: str, freq: int):
        self.char = char
        self.left = None
        self.right = None
        self.frequency = freq
		
    def merge(self, other: 'TrieNode') -> 'TrieNode':
        new = TrieNode('', self.frequency + other.frequency)
        new.left = self
        new.right = other
        return new
		
    def __lt__(self, other: 'TrieNode') -> bool:
        return self.frequency < other.frequency

    def pretty_print(self, indent="", is_left=True):
        if self.right:
            self.right.pretty_print(indent + ("│   " if is_left else "    "), False)

        print(indent + ("└── " if is_left else "┌── ") + str(self.char))

        if self.left:
            self.left.pretty_print(indent + ("    " if is_left else "│   "), True)


def hoffman_coding(msytr: str):
    """
    Builds a hoffman coding trie from the received string
    """
    counter = Counter(mystr)

    tries = [TrieNode(c, v) for c, v in counter.items()]
    heapq.heapify(tries) # builds min-heap from tries list

    while len(tries) != 1:
        tr1 = heapq.heappop(tries)
        tr2 = heapq.heappop(tries)
        new = tr1.merge(tr2)
        heapq.heappush(tries, new)

    return tries[0]
