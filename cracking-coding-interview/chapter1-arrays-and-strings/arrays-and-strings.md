# Strings

## Substring search

Goal: Find pattern of length M in a text of length N. Typically N >> M

pattern -> N E E D L E

text -> I N A H A Y S T A C K N E E D L E I N A


Example of apps can use this: Survillence

Screen scraping --> Extract relevant data from web page

*Example:*
- Find string delimited by <b> and </b> after first occurence of 
pattern Last Trade: <--- For me this is a regex :)

```
# Just find the index of Last trade

start = str.indexOf("Last Trade")
from = str.indexOf("<b>", start)
to = str.indexOf("</b>", from)

price = str.substr(from + 3, to)
```


### First solution: Brute-force

```
def findpattern(text: str, pattern: str) -> int:
    """ Finds pattern in text. If found, returns idx where idx
	represents the idx in which the first occurrence starts. If not found, 
	returns -1
	"""
    n = len(text)
    m = len(pattern)
    for i in range(n):
        for j in range(m):
            if haystack[i + j] != needle[j]:
                break
            if j == m - 1:
                return i
    return -1

```

The above works, but:
- It's runtime is O(N*M), and when both N and M are big, it's quite 
inefficient
- It doesn't take much into account regarding the input
- It will get super slow if the text and pattern are repetitive, give "AAAAAAAAAAAAAAB" as text and "AAAAAB" as pattern
