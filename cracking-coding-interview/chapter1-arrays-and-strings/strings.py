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
    alphabet = ascii_lowercase
    alphlen = len(alphabet)

    letter_to_idx = {letter: i for i, letter in enumerate(alphabet)}
    automaton = [0 for _ in range(m+1)] * alphlen
    automaton = []
    for i in range(alphlen):
        automaton.append([0 for j in range(m+1)])

    for i, letter in enumerate(pattern):
        automaton[letter_to_idx[letter]][i] = i+1

    # To start matching again from the last state
    # Either use lambda transition and without consuming
    # go back to state 0 or add transition from last state
    # to first
    automaton[letter_to_idx[pattern[0]]][m] = 1

    # If we are consuming the first character and
    # we see the first chacater again, then we need
    # to keep in the current state 1!
    automaton[letter_to_idx[pattern[0]]][1] = 1

    state = 0
    for i, letter in enumerate(text):
        state = automaton[letter_to_idx[letter]][state]
        if state == m:
            return i - (m - 1)
    return -1


pattern_finding_functions = [findpattern, findpattern2, knutmorrispratt]

for fn in pattern_finding_functions:
    message = f"Failed w/function {fn}"
    print("Testing ", fn)
    assert 9 == fn("thisisthehaystackajasfdjk", "haystack"), message
    assert -1 == fn("thisisthehaystackajasfdjk", "nope"), message
    assert 7 == fn("aabaaacbaaaaaaa", "baaaa")
