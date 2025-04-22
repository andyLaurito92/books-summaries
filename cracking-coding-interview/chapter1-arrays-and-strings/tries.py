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

Runtime is good, but space that it takes to build this is not good because
we might have a lot of lists with non values. Can we do better?
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

    def delete(self, key: str) -> Any:
        """
        Returns the value of the key to delete. None if
        the key doesn't exist, raises a ValueError
        """

        #1. Find out if the key exists and store path
        # to key
        curr = self
        path = []
        for c in key:
            i = self.letter_to_idx[c]
            path.append((curr, i))
            curr = curr.next[i]
            if curr is None:
                raise ValueError("Key not found ", key)
        
        #2. If we are here, we found the prefix, we need to check
        # if it corresponds to a key
        if curr.value is None:
            raise ValueError("Key not found ", key)

        res = curr.value

        #3. We need to check if we need to delete the path
        # because there's no more prefix
        if any(node for node in curr.next):
            return res # It exists other keys, we don't delete anything

        #4. If we are here, all our next values are empty.
        # We need to delete nodes
        while len(path) > 0:
            if self == curr:
                return # empty trie
            curr, i = path.pop()
            curr.next[i] = None # Delete node, thx Python for handling memory
            if any(node for node in curr.next):
                return res

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

try:
    trie.delete("hoho")
except ValueError as e:
    print(e)

trie.delete("hole")
trie.contains("hole")

trie.get("hola")


"""
Implementation 3: TernaryTrie
"""


class TernaryTrieNode:
    def __init__(self, alphabet: str) -> None:
        self.alphabet = alphabet

        self.charkey = None
        self.value = None
        # next nodes
        self.left = None
        self.right = None
        self.middle = None

    def insert(self, key: str, val: Any) -> None:
        def defineNode(keychar: str) -> 'TernaryTrieNode':
            res = TernaryTrieNode(self.alphabet)
            res.charkey = keychar
            return res
            
        curr = self
        j = 0
        while j < len(key):
            c = key[j]
            if curr.charkey is None:  # Empty trieNode case
                curr.charkey = c
            if c < curr.charkey:
                if curr.left is None:
                    curr.left = defineNode(c)
                curr = curr.left
            elif c > curr.charkey:
                if curr.right is None:
                    curr.right = defineNode(c)
                curr = curr.right
            else:
                j += 1
                if j == len(key):
                    break
                if curr.middle is None:
                    curr.middle = defineNode(key[j])
                curr = curr.middle
        curr.value = val

    def get(self, key: str, default: Any = None) -> Any:
        curr = self
        j = 0
        # hole, j = 0, len(key) = 4, 3
        while j < len(key):
            c = key[j]
            if curr is None:
                return default if default else None
            elif curr.charkey == c:
                j += 1
                if j == len(key):
                    break
                curr = curr.middle
            elif curr.charkey > c:
                curr = curr.left
            else:
                curr = curr.right
        return default if curr.value is None else curr.value

    def startsWith(self, prefix: str) -> set[str]:
        """
        Returns a set of all keys that start with
        prefix. If there are no keys that fulfill
        such condition, returns an empty set
        """
        res = set()
        j = 0
        curr = self
        while j < len(prefix):
            c = prefix[j]
            if curr is None:
                return res
            elif curr.charkey == c:
                j += 1
                if j == len(prefix):
                    break
                curr = curr.middle
            elif curr.charkey < c:
                curr = curr.right
            else:
                curr = curr.left

        tosee = set()
        tosee.add((curr, prefix[0:len(prefix)-1]))
        # TODO: Fix this
        while len(tosee) > 0:
            curr, currprefix = tosee.pop()
            if curr.left is not None:
                tosee.add((curr.left, currprefix))
            if curr.right is not None:
                tosee.add((curr.right, currprefix))
            if curr.middle is not None:
                tosee.add((curr.middle, currprefix + curr.charkey))
            if curr.value is not None:
                res.add(currprefix+curr.charkey)
        return res
            

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def __str__(self) -> str:
        return f"TernaryTrieNode({self.alphabet},{self.charkey},{self.value})"


trie = TernaryTrieNode(ascii_lowercase)
trie.insert("hola", 3)
trie.insert("hole", 8)
trie.insert("holland", 6)
trie.insert("hohoho", 10)

print(trie.startsWith("ho"))

print(trie.get("holland"))
print(trie.get("never", "mydefault"))
print(trie.get("nope"))
print(trie.contains("hole"))
print(trie.get("hole"))

trie.insert("andres", 10)
print(trie.get("andres"))

try:
    trie.delete("hoho")
except ValueError as e:
    print(e)

trie.delete("hole")
print(trie.contains("hole"))

print(trie.get("hola"))

