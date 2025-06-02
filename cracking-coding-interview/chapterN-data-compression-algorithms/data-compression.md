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





