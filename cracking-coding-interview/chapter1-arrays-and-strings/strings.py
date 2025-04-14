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


pattern_finding_functions = [findpattern, findpattern2]

for fn in pattern_finding_functions:
    message = f"Failed w/function {fn}"
    print("Testing ", fn)
    assert 9 == fn("thisisthehaystackajasfdjk", "haystack"), message
    assert -1 == fn("thisisthehaystackajasfdjk", "nope"), message
