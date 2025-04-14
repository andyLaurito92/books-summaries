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


