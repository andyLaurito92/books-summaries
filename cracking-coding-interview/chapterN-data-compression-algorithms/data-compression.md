This notes come from course Introductions to Algorithms - Part 2 from Sedgwick

## Compression Idea

To reduce the size of a file

*What for?*

2 main ideas:

- To save *space* when storing it
- To save *time* when transmitting it

*Note* Most of the files have a lot of redundancy!


*Idea* Even though it's true that its seems a bit odd being studying this when we have so large
storage capacity + compute capacity, what we really want to use that more storage and capacity for
is to update *data that has quality*, meaning, I don't want to waste more memory and internet 
throughput in *bad data quality*!

So our goal is to reduce redundancy so we can do more w/the space available

## A bit of history

- The basic concepts go back to 1950!

## Applications

### File compressions

- files: gzip, bzip, 7z
- archives: pkzip

### Multimedia

- Images: gif, jpeg
- Sound: MP3
- Video: MPEG, DivX, HDTV

### Communication

- Skype
- Data compression enabled fax!

### Databases

- Google, meta

## Looseless compression and expansion

We are gonna consider looseless compression, this is:

Given a message which is binary data _B_ 
we want to ble able to compress it applying _C(B)_,
and uncompress it getting our original message _B_

Our goal is that _C(B) <<< B_ where we are measuring 
number of bits

We are gonna measure our algorithms by using

### Compression Ratio

Defined by _bits in C(B) / bits in B_

Ex: 50/75% compression ratio for natural language

### Example: Genomic code

*Genome* String over the alphabet {A, C, T, G}

*Goal:* Encode an N-character genmoe: ATAGATGCATAG...

Now, let's say we are in Java, the above alphabet is ASCII letters. The standard ASCII 
representation in bites is *8 bits per char*

bits(message) = bits(ATAGATGCATAG...) = 8 bits * len(str)

Now: Do we really need 8 bits to represent just 4 letters? :) NO!

We could just use 2bits!

So used *fixed-length* codes: k bits support an alphabet of 2^k elements


#### History

Initially in the 90's, a genomic database used ASCII characters to encode what could have been encoded
in a more compact way!


### Tools

We need to read binary inputs and write binary outputs

## Universal data compression

*Proposition:* No algorithm can compress every bitstring! (a bitstring is a sequence of binary digits (bits))

Proof: By the absurd, if you have an algorithm that can compress every bitstring, just apply the algorithm to the original 
message until you get a 0 length encoded message, which doesn't make sense



## Run-length encoding

*Idea* Usually we have in a message of bits long runs of repeated bits

Instead of writing all the bits, why don't we just cound the number of bits we have in this sequence?

So if we have 000000111111000000111111 (6 0's followed by 6's 1 followed by 6 0's again followed by 6 1's again), why don't
we just write the count?

So the *representation* would be: 4bits count to represent 0s and 1s, and then use [bit][count]

Therefore the above message representation would be 00110101100011010110

len(message) = 6*4=24 bits
len(C(M)) = 4*(1+4) = 20 bits

compression ratio = 20 bits / 24 bits = 0.83%

You can also read the above as: *"You are saving 16.7% by compressing this file using this algorithm"*

*Note* In how many bits shall we represent the count? :) If we store too many bits, we could be creating a C(B) >> B ! So 
we should take into consideration this number. If it's too low, then we might have multiple repeated chains when we could have
done better. 


Application of the above: JPEG


## Huffman encoding

This time, we use variable-length codes!, this is, use different number of bits to encode different chars

*Problem* We introduce ambiguity!

Ex: Morse code!

*Why does introducing a variable-length code introduces ambiguity?*

Because we have codewords that are prefix of other codewords!

Then, *idea*. Avoide the above :)

How? 

Ex1: fixed length code
Ex2: Add a *special stop character* to each codeword
Ex3: *General prefix-free code*

We are gonna study here the third option. How do we represent the above? By using tries!

## Trie representation

Use a binary trie that:

- Chars in leaves
- Codeword is path from root to leaf


There are several things that we need to consider by using this trie.

1. (*Writing*) We need to be able to grab that trie structure, and transform it into bits. This will be a message
that we will need to send with the file so that we can reconstruct the trie in memory. 
The size of the trie in bits will be much smaller that the size of the message we are encoding, so we should
be good :)
2. (*Reading*) We need to be able to read the trie structure sent to us in bits format
3. (*Creating a prefix-free tree*) For this, we use can use Shannon-Fano coding (suboptimal) or Hoffman coding (optimal)

### Shannon-Fano coding

This is not an optimal solution! Meaning, it does not always achieve the lowest possible expected codeword length

- Partition symbol S into 2 substes: Sa and Si of (roughly) equal freq
- Codewords for symbols in Sa start with 0; for symbols in Si start w/1
- Recur in Sa and Si


### Hoffman coding


- Count frequency for each character in input (in Python, we use `from colletions import Counter`. *Goal* For those characters that have the highest frequency, we want to use the less amount of bits possible!. The less frequency, the more bits
- Start w/one node for each character with with equal to frequency
- Select two tries with min weight and merge into single trie with
cumulative weight


```

from collections import Counter
import heapq

mystr = "ABADACADABRA!"

counter = Counter(mystr)

class TrieNode:
	def __init__(self, char: str, freq: int):
		self.char = char
		self.left = None
		self.right = None
		self.frequency = freq
		
	def merge(other: 'TrieNode') -> 'TrieNode':
		new = TrieNode(None, self.frequency + other.frequency)
		new.left = self
		new.right = other
		return new
		
	def __lt__(other: 'TrieNode') -> bool:
		return self.frequency < other.frequency
	
	def __str__(self) -> str:
		return self.char


tries = [TrieNode(c, v) for c, v in counter.items()]
heapify(tries) # builds min-heap from tries list

while len(tries) != 1:
	tr1 = heappop(tries)
	tr2 = heappop(tries)
	new = tr1.merge(tr2)
	heappush(tries, new)
```
