Useful to remember and know how to do them. Usually used for optimization. In C, this is actually handy :)

## Brushing up a bit

- 0110 + 0010 = 1000 (6 + 2 = 8)
- 0011 + 0010 = 0101 (3 + 2 = 5)
- 0110 - 0011 = 0011 (6 - 3 = 3) Remember that when u borrow 1 from the left operand, u substract 2 - 1 (as in decimal, u substract 10 - X)

Note that A - B = A + (~B + 1), 2s complement. This is what most CPUs do under the hood
In the example above, it would be:
0110 + 1100 + 1 = 10010 + 0001 = 10011, we ignore overflow = 0011

*Remember:* CPUs have word size, in other words, the width of the registers, other words, the number of bits a register has. 

So if the CPU has 64 word size, as x86-64, ARM64 (Apple M1/M2), usually you will have ints of 32 bits. If we have 32 bits, then the 
~B being B = 3 would look sht like this:
B = 00000000_00000000_00000000_00000011 => ~B = 11111111_11111111_11111111_11111100 + 1  = 11111111_11111111_11111111_11111101
and now you do B + A, where A =00000000_00000000_00000000_00000110 and that gives overflow that ends up givint you 00000000_00000000_00000000_00000011
which is the correct result

## Notes:

In C, an int is 32 bits, a long is 64 bits and void* is 64 bits

In Python, an int is more complex to be defined :D
- From a user perspective, you don't really care. CPython handles everything for you
- From a Cpython developer perspective:
	- int can be of vary size: An int *is not limited by the word size of the platform*
	- You can store numbers larger than 64 bits in a variable, ex: 2**100
	- How? Because CPython internally stores small integers using fixed-with types internally
	- *Automatically* switches to a big number representation (bignum) when needed. This is implemented using a struct w/array of digits
	(base -2**30 or base -2**15 depending on the build)
	
CPython uses a struct called PyLongObject that can be found [here](https://github.com/python/cpython/blob/main/Include/cpython/longobject.h)

Python uses a base -2**n representation internally
- Python int is represented as an array of digits
- Each digit is a chunk of the number in base 2**30 on 64-bit system
- Ex: 2**60 + 123 is split into chunks that are 30 bits wide :O

Why Python uses 30 bits and not 32/64? So that operations don't overflow :)

In C, you have many integer types that are in the `#include <stdint.h>`


## Bitwise operation

### Shift ( << )

a << b means "shift the bits of _a_ to the left by _b_ positions", filling the right with zeros

a << b it's equivalent to a * 2^b

*Examples*

- 1 << 0 -> 1
- 1 << 1 -> 2
- 1 << 2 -> 4
