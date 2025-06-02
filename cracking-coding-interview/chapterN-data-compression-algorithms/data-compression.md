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
