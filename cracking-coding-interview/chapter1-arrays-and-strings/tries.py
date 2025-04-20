from typing import Any, Optional
from string import ascii_lowercase

"""
Implementation 1
"""
trie = {} # null node represented as empty dict
for key, value in [("cat", 4), ("car", 3), ("cart", 2), ("dog", 1), ("dot", 0)]:
    node = trie
    for char in key:
        node = node.setdefault(char, {})
    node["*"] = value  # "*" marks the end of a word


"""
Implementation 2
"""
class TrieNode:
    def __init__(self, alphabet: str):
        self.len_alphabet = len(alphabet)
        self.alphabet = alphabet
        self.letter_to_idx = {letter:i for i, letter in enumerate(alphabet)}
        self.value = None
        self.next = [None] * self.len_alphabet

    def insert(self, key: str, value: Any) -> None:
        curr = self
        for c in key:
            i = self.letter_to_idx[c]
            if curr.next[i] is None:
                node = TrieNode(self.alphabet)
                curr.next[i] = node
            curr = curr.next[i]
        curr.value = value

    """
    def insert(self, key: str, value: Any) -> TrieNode:
    	return self.insert_recursive(self, key, value, 0)

    def insert_recursive(self, node: 'TrieNode', key: str, value: Any, d:int) -> TrieNode:
    	if node is None:
    		node = TrieNode(self.alphabet)
    	if d == len(key):
    		node.value = value
    		return node
    	node.next[char_to_idx(key[d])] = self.insert_recursive(node.next[char_to_idx[key[d]]], key, value, d+1)
    	return self
    """

    def search(self, key: str) -> Optional[int]:
        curr = self
        for c in key:
            i = self.letter_to_idx[c]
            curr = curr.next[i]
            if curr is None:
                return None
        return curr.value

    def contains(self, key: str) -> bool:
        return self.get(key) is not None


    def get(self, key: str, default: Any = None) -> Any:
        curr = self
        for c in key:
            curr = curr.next[self.letter_to_idx[c]]
            if curr is None:
                return default if default else None

        return curr.value

    def startsWith(self, prefix: str) -> set[str]:
        """ Return all keys stored in the dictionary that
        starts with prefix
        """
        res = set()
        curr = self
        # First: find the prefix
        for c in prefix:
            i = self.letter_to_idx[c]
            if curr.next[i] is None:
                return res
            curr = curr.next[i]

        # Second: If we are here, is because we have keys stored with
        # this prefix! Start collecting keys
        radix = self.len_alphabet
        tosee = set()
        tosee.add((curr, prefix))
        while len(tosee) != 0:
            curr, currprefix = tosee.pop()
            for i in range(radix):
                if curr.next[i] is not None:
                    tosee.add((curr.next[i], currprefix + self.alphabet[i]))
                if curr.value is not None:
                    res.add(currprefix)
        return res


trie = TrieNode(ascii_lowercase)
trie.insert("hola", 3)
trie.insert("hole", 8)
trie.insert("holland", 6)
trie.insert("hohoho", 10)

print(trie.search("hola"))

print(trie.search("hehehe"))

print(trie.startsWith("ho"))

print(trie.get("holland"))
print(trie.get("never", "mydefault"))
print(trie.get("nope"))
trie.contains("hole")
