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

## R-way Tries

*Read the intro above to understand why we need to use them (most of the times the
use case involves prefix search)*

Etimology: Middle letters of re*trie*val :O 

Given R radix (= number of characters)

- Tree structure of nodes where we store characters
- Each node has R childrens, one for each possible character
- store values in nodes corresponding to least characters in keys

Given the following dictionary:

```
mytrie = {"cat": 4, "cart": 3, "car": 2, "dog": 1, "dot": 0}
```

The following is the representation of the internal trie structure

```
(root)
 ├── c
 │   └── a
 │       ├── t  [✓ 4]
 │       └── r
 │           └── t  [✓ 3]
 │           [✓ 2]
 └── d
     ├── o
         ├── g  [✓ 1]
         └── t  [✓ 0]

```

And a naive implementation can be the following:

```
trie = {} # null node represented as empty dict
for key, value in [("cat", 4), ("car", 3), ("cart", 2), ("dog", 1), ("dot", 0)]:
    node = trie
    for char in key:
        node = node.setdefault(char, {})
    node["*"] = value  # "*" marks the end of a word
```

For a more robust implementation, see implementation section implementation

### Search in a trie

Follow links corresponding to each character in the key
- *Search hit*: We consume all characters and found in the last node a value. If null then this is a search miss
- *Search miss*: Either we couldn't consume all characters or we got into the last character
and value was null

### Insertion into a trie

Follow links corresponding to each characer in the key:
- Encounter a null link: create new node
- Encounter the last character of the key: set value in that node

### Implementation

One approach is the one presented above, done by chatgpt :D. The other one (proposed in the course) is to
create a TrieNode and define next as a list of nodes. Now the "cool" things of this is that we don't
need to *explicitly* store the characters!

```
from typing import Any, Optional

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
				self.next[i] = node
			curr = curr.next[i]
		curr.value = value
	
	def search(self, key: str) -> Optional[int]:
		curr = self
		for c in key:
			i = self.letter_to_idx[c]
			curr = curr.next[i]
			if curr is None:
				return None
		return curr.value
		
	def startsWith(self, prefix: str) -> set[str]:
		"""
		Return all keys stored in the dictionary that 
		starts with prefix
		"""
		res = set()
		curr = self
		prefix = []
		for c in prefix:
			i = self.letter_to_idx[c]
			if curr.next[i] is None:
				return res
			prefix.append(c)
			res.add(''.join(prefix))
		return res
			
```

In the above representation, a character is just represented by a non-none entry in the
node.next list.

### Summary

- Good data structure when the alphabet is small. Think that nowadays, Unicode version 16 has 155063 characters :)
- They can be super memory inefficient when you have many elements in the data structure becase
you have to create a list of size R where most of the elements are None. This will cause out of 
memory for large datasets
- *IMPORTANT NOTE* When having a miss search, tries work much faster than symbol tables that use
hashing! Why? because they don't have to read the *WHOLE STRING* to find out that the string
is not there

How to overcome the above issue? Keep reading :)

## Ternary search Tries (another trie implementation)

*Idea* Instead of storing as children a list of size radix, store 3 characters: left, middle, right. 
For inserting into the trie, we follow these rules:
- If we reach an empty node, define the node and put as middle node the current char
- If current character match the character in the middle, follow that link and cosume current char 
- If there's non-matching character:
	- If the current character is less than the link in the middle, follow the left link
	- If the current character is greater than the link in the middle, follow the right link

In this implementation, we store both the character and the value in the node. 

*Questions:* 
- How do we define the middle character to define lower and higher characters? That depends on the first insertion we do. This is gonna be the keychar
- What happens when we have unbalanced tries?

*Summary*

TST are as fast as hashing but much more space performant

## Trie running time and space table comparisson
| implementation           | search hit   | search mis | insert   | space (reference) |
| red-black BST            | L + c lg^2 N | c lg ^ N   | c lg ^N  | 4 N               |
| hashing (linear-probing) | L            | L          | L        | 4N to 16 N        |
| R-way Trie               | L            | log_r N    | L        | (R+1)* N          |
| Ternary search trie      | L + ln N     | ln N       | L + ln N | 4N                |
|                          |              |            |          |                   |


## An hybrid: Using both R-way Tries and Ternary search tries both together

*Idea* 
- Do R^2 way branching at root
- Each of R^2 root nodes points to a TST

### Character-based operations supported by tries

- Prefix search: This is used in autocomplete apps, search bars, text editors, IDEs, shells, u name it! 
- Ordered keys: 
- longest prefix: Find longest key in symbol that is a prefix of query string. This is used for sending packets toward destination IP addresess. Router chooses IP address in routing table that is longest prefix match!
The longest the IP, the more specific it is for sending the packet

## TODO: Patricia Trie (radix trie)

Look more about this. Instead of having one-way branching (this is, one branch per chatacter), have nodes
that represent sequence of characters.

I didn't find anything about patricia tries in either algorithms by sedgewick or in cormen

## TODO: Suffix tries

Look more about this. Used in computational biology. Could be useful for the concatenated word problem

Advanced data structures by peter brass has some info on this

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

Useful when back up in the original text is not a problem. The idea is to 
scan the pattern from right to left when trying to match it against the text.
When we found a mismatch, we slide the text len(pattern) to the right.

Example:
If we have a pattern like: `BAABBAA`, we start from right to left:
- A matches? Yes? next character left
- A matches? Yes? next character left
- B matches? No? Jump len(pattern) and start again.

Text = BAABBCBAABBAAD

*Question:* Couldn't it happen that you jumped to much?

The answer is yes, and this is why we need an array of restart positions!
Another way is to decide what to do next on the basis of the character 
that caused the mismatch in the *text* as well as the pattern.

*Idea*: For each preprocessing step we need to decide, for each possible character
that could occurd in the text, what we would do if that character were to cause 
the mismatch. The idea here is to check whether the character (X) belongs to the pattern
or not. If (X) it does belong to the pattern, then we could slide the pattern to match 
the right most character that matches X. We then start matching 

*Starting point:* To implement the mismatched charcater heuristic, we use an array
right that gives, for each character in the alphabet, the index of its rightmost 
occurrence in the pattern (or -1 if the character is not in the pattern)

*Runtime complexity:* On typical inputs, substring search uses ~ N/M character comparissons
to search for a pattern of length M in a text of length M



### Rabin-Karp

*Basic idea:* Use modular hashing -> Take a big prime, compute the reminder
- compute a hash of pattern characters 0 to m-1
- for each i, compute a hash of text characters i to m + i -1
- if pattern hash = text substring hash, check for a match


Without thinking the above a bit, having to calculate the new hash per each text[i...i+m]
can be supper inefficient. How can we do this better?

#### How to compute the hash function?

Using the notation t_i, for txt[i], we wish to compute:

```
x_i = t[i]*R^(M-1) + t[i+1]*R^(M-2) + ... + t[i+m]*R^0 (mod Q)
```

M-digit, base-R integer, modulo Q

*Hornern's method:* Linear-time method to evaluate degree M polynomial

Assuming decimal number, R = 10, then:

```
def hash(key: str, m: int):
	long h = 0
	for j in range(m):
		h = (R * h + key[j]) % Q
	return h
```


*Note* Given that we are talking about hashing comparisson, we later need to check
(if we want to be exact), whether we had a hash colission or if we really find 
the substring we were looking for. 

The version of the algorithm that doesn't check for a real match but assummes 
equality by comparing hashes is called "the montecarlo version".

*In theroy*, if Q is sufficiently large random prime (about M * N^2), then 
the probability of a false colission is about 1/N.

*In practice*, take a large prime that doesn't cause overflow :)

Running time: O(N + M)


#### Why do we care about this algorithm?

- There are simple algorithms, such as the automaton state algorithm, that works perfect
in linear time. Then why shall we care about this one?

*Because*

1. Easy to extends to 2d patterns. 
2. Easy to extends to finding multiple patterns!

For the second case, you just need to:
- Compute the hashes for those patterns
- Look for any of those using a symbol table

Disadvantages
- For substring search, is a bit slower, bc of the arithmetic operation 
- If you want the las vegas search, you need to backup


### Sliding window 

#### Intro

This section doesn't come from neither cracking the coding interview nor any algorithm books but
comes from having to deal with longest repeating character replacement problem (see programming-exercises
repo to see the description of this problem).

After the above, I realised that there are several algorithmic tecniques not covered in the mentioned books.
A good resource for studying these content then is https://www.designgurus.io/course/grokking-the-coding-interview

Unfourtunately the above course is paid. Because of that, it's sometimes better to just see topics and look for 
them in chatgpt/internet. 

Some free material about this topic:
1. https://www.hellointerview.com/learn/code/sliding-window 
2. https://www.geeksforgeeks.org/window-sliding-technique/


#### Now yes, sliding window

Template

```
def variable_length_sliding_window(nums):
  state = # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # extend window
    # add nums[end] to state in O(1) in time

    while state is not valid:
      # repeatedly contract window until it is valid again
      # remove nums[start] from state in O(1) in time
      start += 1

    # INVARIANT: state of current window is valid here.
    max_ = max(max_, end - start + 1)

  return max_
```

*When to use it?*


When you have a question that involve searching for a substring (continuos subsequence) in 
an array or a string.
