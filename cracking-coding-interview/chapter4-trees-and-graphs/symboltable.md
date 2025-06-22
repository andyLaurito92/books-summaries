# Symboltable

We usually directly jump into "hashmap" or think on a hash function when we talk about
associating a tuple (key, value). But reallity is that we have a lot of different data
structures that can help us on this association. In this section we will talk about
those


## API

*Idea*: Associate values

- key-value pair abstraction
- Insert a value w/specified key
- Given a key, search for the corresponding value

```
from typing import Iterator 

ST()

put(key: Key, value: Value): None
get(key: Key): Value
delete(key: Key): None
contains(key: Key): bool
isEmpty(): bool
size(): int
keys(): Iterator[Key]

```

## Usage examples:

- DNS lookup: (url, ip)
- genomics: (dna string, known positions)
- web search: (keyword, list of pages)
- Infinite more :)


## Types of Key and Values

- `Value` can be anythin
- `Key` usually must be:
	- Comparable
	- hashable
   
Given that our symbol table will use heavily the equal operator, is worth remembering a rule of thumb
for defining custom equality on user classes:

### Receipe for checking equality between objects

- Check against null
- Check that two objects are of the same type
- Compare each significant field
	- If field is primitive type, use ==
	- If field is object, use equals (in Java)
	- if field is an array, apply to each entry (in Java -> Arrays.equals)


## Implementations of symbol table

The following implementations can be found in file `symboltable.py`

1. Use a linked list
	1.1. O(N) complexity for adding, removing, searching elements. Not ideal but works
2. Use a sorted array
3. Use a binary search tree (already allows us to perform ordered operations)


## CPython and trees

CPython doesn't include any tree structure in its core. The main reason is its philosophy of "keep it simple". 
Usually a hashmap structure, as how dict structure is built from, will generally include all the use cases
you need for your usual app. 

If you need some sort of "sorted dictionary", there are some libraries you can include:

- [Python sorted containers](https://github.com/grantjenks/python-sortedcontainers)

### dict preserves insertion order

Since CPython 3.7+, dict `preserves insertion order`. This means that if you write the following program:

```
x = {1: "hey", 3:"ho", 2:"haha", -1: "asfjlka"}
for key, val in x.items():
	print(key, val)
```

Result will be:

```
1 hey
3 ho
2 haha
-1 asfjlka
```
