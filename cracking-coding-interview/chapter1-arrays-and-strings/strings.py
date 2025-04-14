"""Brute force """
def findpattern(haystack: str, needle: str) -> int:
    """ Finds needle in haystack. If found, returns idx where idx
	represents the idx in which the first occurrence starts. If not found, 
	returns -1
	"""
    n = len(haystack)
    m = len(needle)

    i = 0
    j = 0
    while i < n:
        while i < n and haystack[i] != needle[j]:
            i += 1
            if i == n:
                return -1

            start = i
            while i < n and j < m and haystack[i] == needle[j]: 
                i += 1
                j += 1

            if j == m:
                return start
            else:
                j = 0
    return -1
