"""Brute force """
def findpattern(haystack: str, needle: str) -> int:
    """ Finds needle in haystack. If found, returns idx where idx
	represents the idx in which the first occurrence starts. If not found, 
	returns -1
	"""
    n = len(haystack)
    m = len(needle)
    for i in range(n):
        for j in range(m):
            if haystack[i + j] != needle[j]:
                break
            if j == m - 1:
                return i
    return -1



"""
In Python, the algorithm used is a mix between Boyer-moore and
Horspool algorithm. Read more about this here:

https://stackoverflow.com/questions/36868479/python-str-index-time-complexity

http://www.laurentluce.com/posts/python-string-objects-implementation/

https://softwareengineering.stackexchange.com/questions/183725/which-string-search-algorithm-is-actually-the-fastest
"""


# ABACABAA
# BAA

# i = 1, j = 0
# 
def findpattern2(text: str, pattern: str) -> int:
    """ Still brute force, but changing something: Now i points to
    the end of the sequence of already-matched chars in text and
    j stores # of already-matched chars (end of sequence in pattern)
    """
    n = len(text)
    m = len(pattern)

    j = 0
    i = 0
    while i < n and j < m:
        if text[i] == pattern[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1

    if j == m:
        return i - m
    else:
        return -1


from string import ascii_lowercase


def buildautomaton(pattern: str, alphabet: str) -> list[list[int]]:
    k = len(alphabet)
    m = len(pattern)
    letter_to_idx = {letter: i for i, letter in enumerate(alphabet)}
    automaton = []
    for i in range(k):
        automaton.append([0 for j in range(m+1)])

    # To start matching again from the last state
    # Either use lambda transition and without consuming
    # go back to state 0 or add transition from last state
    # to first
    automaton[letter_to_idx[pattern[0]]][m] = 1

    # If we are consuming the first character and
    # we see the first chacater again, then we need
    # to keep in the current state 1!
    automaton[letter_to_idx[pattern[0]]][1] = 1

    # Simulate what happens when we find char
    # c != pattern[i] in the ith position after
    # matching suffix pattern[1..i-1]
    # For this, we simulate state X
    statex = 0
    for i, letter in enumerate(pattern):
        if i == 0:
            automaton[letter_to_idx[letter]][i] = i+1
            continue

        # IMPORTANT STEP: NON MATCHING CHARACTERS
        for c in alphabet:
            automaton[letter_to_idx[c]][i] = automaton[letter_to_idx[c]][statex]

        automaton[letter_to_idx[letter]][i] = i+1

        # Move state X to state that would become of matching
        # the previous character (Remember that we are matching
        # suffix pattern[1..i]), this is, pattern shifted 1
        statex = automaton[letter_to_idx[pattern[i]]][statex]
    return automaton


def knutmorrispratt(text:str, pattern: str) -> int:
    """
    We build an automaton to match the pattern in the text
    This takes O(m*alphabet) space and O(m) time, where
    m = len(pattern) and alphabet = len(# characters) we can
    encounter in the pattern

    For our example, lets assume ascii_lowercase
    """
    n = len(text)

    if n < 2:
        # run brute-force, will still give O(N)
        return findpattern2(text, pattern)

    m = len(pattern)
    alphabet = set(text) | set(pattern)
    letter_to_idx = {letter: i for i, letter in enumerate(alphabet)}
    automaton = buildautomaton(pattern, alphabet)
    state = 0
    # O(N)
    for i, letter in enumerate(text):
        state = automaton[letter_to_idx[letter]][state]
        if state == m:
            return i - (m - 1)
    return -1


def matching_from_input(pattern: str) -> None:
    m = len(pattern)
    automaton = buildautomaton(pattern, ascii_lowercase)
    state = 0
    while True:
        state = automaton[input()][state]
        if state == m:
            print("Pattern found!")


def bayermoore(text: str, pattern: str) -> int:
    """
    Implements bayer-moore algorithm to find pattern
    in text. Returns first occurrence of pattern or -1
    if no ouccrrence exists.
    NOTE: Assumes ASCII characters
    """
    def charidx(charstr: str) -> int:
        """
        Return the idx of the char
        """
        return ord(charstr) - ord('a')

    right = [-1] * len(ascii_lowercase)
    m = len(pattern)
    n = len(text)
    for j in range(m):
        # Set char to rightmost appearance in pattern
        right[charidx(pattern[j])] = j

    i = 0
    skip = 0
    while i < n - m:
        skip = 0
        for j in reversed(range(m)):
            if pattern[j] != text[i+j]:
                skip = j - right[charidx(text[i+j])]
                if skip < 1:
                    skip = 1
                break
        if skip == 0:
            return i
        i += skip
    return -1

import math

class RabinKarpSearch:
    # R = 256 because ASCII characters
    def __init__(self, pattern: str,
                 R:int = 256, Q:int = 997):
        self.R = R
        self.Q = Q  # Big prime
        self.pattern = pattern
        self.RM = 1
        self.patthash = self.hash(pattern)
        # precompute R^M-1 (MOD Q)
        for j in range(len(pattern) - 1):
            self.RM = (self.R * self.RM) % self.Q

    def hash(self, pattern: str) -> int:
        h = 0
        for j in range(len(pattern)):
            h = (self.R * h + ord(pattern[j])) % self.Q
        return h

    def search(self, text:str) -> int:
        """
        Find first occurrence of pattern in txt
        """
        n = len(text)
        m = len(self.pattern)
        txthash = self.hash(text[:len(self.pattern)])
        if self.patthash == txthash:
            return 0 # Montecarlo implementation; Don't care about hash colission

        for i in range(m, n):
            txthash = (txthash + self.Q - self.RM*ord(text[i-m]) % self.Q) % self.Q
            txthash = (txthash * self.R + ord(text[i])) % self.Q
            if self.patthash == txthash:
                return i - m + 1
        return -1



pattern_finding_functions = [findpattern, findpattern2, knutmorrispratt, bayermoore]

for fn in pattern_finding_functions:
    message = f"Failed w/function {fn}"
    print("Testing", fn.__name__)
    assert 9 == fn("thisisthehaystackajasfdjk", "haystack"), message
    assert -1 == fn("thisisthehaystackajasfdjk", "nope"), message
    assert 7 == fn("aabaaacbaaaaaaa", "baaaa")
    assert 8 == fn("aaaaabaaaabbaaaaa", "aabbaa")



rk = RabinKarpSearch("haystack")
assert 9 == rk.search("thisisthehaystackajasfdjk")

rk1 = RabinKarpSearch("baaaa")
assert 7 == rk1.search("aabaaacbaaaaaaa")
