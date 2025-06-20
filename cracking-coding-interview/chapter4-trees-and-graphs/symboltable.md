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
