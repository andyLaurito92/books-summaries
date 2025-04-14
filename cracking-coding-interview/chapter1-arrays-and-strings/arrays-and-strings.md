# Strings

This info is coming from the algorithms-part2 coursera course (Robert Sedgewick)

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
- It needs to *backup*!

#### The backup problem

The bruteforce algorithm presents one more problem: When we start looking for the pattern, we start consuming the text.
If it doesn't match, let's say after k characters, then we move i 1 position. BUT this means *"going back to the i+1 position"*
which was already processed!

This works for a static string, but if we are looking into a stream or standard input, or whatever structure that doesn't 
allow us to backup, then the above algorithm doesn't work

The bruteforce algorithm needs to backup every mismatch!

### Second solution: Brute-force alternate approach

In this algorithm, 
- i points to end of sequence of already-mattched chars in text
- j stores # of already-matched chars (end of sequence in pattern)

```
def findpattern(text: str, pattern: str) -> int:
    """ Finds pattern in text. If found, returns idx where idx
	represents the idx in which the first occurrence starts. If not found, 
	returns -1
	"""
    n = len(text)
    m = len(pattern)
	j = 0
	i = 0
	while i < n and j < m:
        if text[i] == pattern[j]:
			i += 1
			j += 1
		else:
			i =- j # backup!
			j = 0
	
	if j == m:
		return i - m
	else:
		return -1

```

The above implementation does exactly the same, but it explicitly shows how we backup 
i each time we have a mismatch between the text and the pattern


*Questions:* 
- Theoretical: Can we do better than O(N*M)? Can we do in O(N)?
- Practical: Can we avoid the backup in the text stream? --> This actually can make
our algorithm not to work in every situation!


### Knuth-Morris-Pratt substring search


