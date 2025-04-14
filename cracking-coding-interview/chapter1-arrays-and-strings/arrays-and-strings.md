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
def findpattern(haystack: str, needle: str) -> int:
	""" Finds needle in haystack. If found, returns idx where idx
	represents the idx in which the first occurrence starts. If not found, 
	returns -1
	"""
	n = len(haystack)
	m = len(needle)

	j = 0
	i = 0
	while i < n:
		while i < n and haystack[i] != needle[j]:
			i += 1
			
		if i == n:
			return -1
			
		start = i
		while haystack[i] == needle[j] and i < n and j < m:
			i += 1
			j += 1
		
		if j == m:
			return start

	return -1
		
```
