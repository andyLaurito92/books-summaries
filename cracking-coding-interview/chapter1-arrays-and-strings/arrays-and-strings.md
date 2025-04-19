# Strings

This info is coming from the algorithms-part2 coursera course (Robert Sedgewick)

This section is divided into 2 subparts:
1. *Tries implementation:* 

Why do we need to use tries? 

A first tought could be the following: Reading a string for getting it's hash takes len(str). Given that I want to perform this operation many times, then this is too expensive.

To the above thinking, in CPython reallity is much brighter :). Because strings are immutable,
CPython cache the hash value of the string!. This means that dict["hola"] is O(1) amortized. Therefore, saying that we will study tries to get *an exact match* faster than a hashing function doesn't really make sense.

Then why?

The key is in the word *exact*. Yes, if we want an exact match, hasing is better. However, if 
what we want to match are *prefixes*, then tries perform way better! A dictionary 
implemented using hashing + open addressing cannot handle prefixes. You need the entire
string to find the value associated to it

In which cases could we need the above?

- *Autocomplete*: Start typing and get all strings that contain the prefix
- *Prefix search*: Get all gene names that start with prefix
- *Whatever problem related to prefixes*
- *Range queries*: All words between 'cat' and 'caz' (defined by lexicographical order)
- *Finding if a string can be broken into words from a dictionary*
- *Matching words in a large text stream*


2. Substring search, this is, given a pattern M and a text S, we want to find how many 
times the pattern N repeats in S. Usually, len(M) <<< len(S). Algorithms we will study 
in this section:
- Knuth-Morris-Pratt
- Deterministic finite automaton
- Bayer-moore
- Rabin-Karp

## Tries

Read the intro above to understand why we need to use them (most of the times the
use case involves prefix search)

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

*Intuition:* The brute-force algorithm is not considering the chatacters read!
If you have `ABAAABAAAAA` and you are trying to match `BAAAA`, the brute-force
algorithm tries to match the pattern, but when it doesn't find it, it backups 
to the first character after B (in the above example), which is A, and keeps 
repeating this until next B. This doesn't make sense since we know that the 
pattern doesn't start with that character :)

KMP algorithm simple keeps iterating and doesn't backup i in the above case

*Take away* It always avoid backup

*Note:* In the coursera course by sedgewick, the next algorithm is presented
as the Knuth-Morris-Pratt algorithm, however in Cormen and other places (such 
as wikipedia), the next algorithm is just presented as "String matching with
finite automata" and the Knut-Morris-Algorithm is another one.


#### DFA: Deterministic finite state automaton

Idea: Build an automata to match the pattern --> Right, but then it's a regex :)

What is an automata for matching a pattern?
- Finite number of states including start and halt
- Exactly one transition for each char in alphabet
- Accept if sequence of transitions lead to halt state


*How do we represent the automaton?*

By using a matrix. We have columns representing the state of the automaton and 
each row represents what state to take given the current character. 

How many rows do we have? 1 per character in the alphabet
How many columns do we have? 1 per character in the pattern + 1 (the initial state)


What does a state mean in the automaton? It's the number of characters in pattern
that have been matched! So it's also giving us suffixes


*Differences between brute-force algorithm and Knut-Morris-Pratt algorithm*

- We don't backup
- We need to build the automaton before we start consuming the text

Because we don't backup, we can use the above algorithm to match 
strings in a stream of characters! See pattern_matcher_fron_input.py script
for a demo


#### How to build the automaton?

- For the matching part, easy: Just create 1 state per character and make
the transitions move to the next state when the char is matched, this is:
```
automaton = [ [0] * (len(pattern) + 1) for _ in range(len(alphabet))]
for i, char in enumerate(pattern):
	automaton[letter][i] = i + 1
	
When we have a state that equals len(pattern) we have found our pattern!

TIP: If the text to search is previously known, we can reduce the alphabet
to alphabet = set(text) | set(pattern)
```

- For the mismatch part is trickier, because it depends on the state 
we are what we need to do next. The trick here is to understand the prefixes
we have already consumed and to move to the state that matches the prefixed 
consumed

If we find a mismatch, this is, c != pattern[j] for some j, then if we remember, 
j represented the number of characters matched for the pattern. Given this, we DO know
that the previous 1..j-1 characters matched the pattern[0..j-1]. What we could do
then is simulate pattern[0..j-1] on the DFA and take transition c, where c is the 
character that is a mismatch

The running time of this *seems to require j steps* if we simulate the pattern[0..j-1].
*Can we do better?* YES -> Keep track of the previous state, this is, keep a state X
that is behind 1 state, and when a mismatch occur, then just consume the char c from X. 
This can be done in O(1) and will tell you in which state we should be

Yes, but this has to be done for each element of the alphabet, which makes the above 
O(len(pattern) * len(alphabet)). If the alphabet is capped, which usually is, then we are good because
we can take it as a constant time


*Reminder about suffixes*

A string s is a suffix of a string t if there exists a string p such that t = ps. 
A proper suffix of a string is not equal to the string itself. 

A more restricted interpretation is that it is also not empty. A suffix can be seen as a special case of a substring. 


### Knuth-Morris-Pratt substring search (according to Cormen)

TODO


### Boyer-Moore algorithm

Invented by Robert Boyer and J.Strother Moore
