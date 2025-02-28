Dynamic programming is mostly just a matter of taking a recursive
algorithm and finding the overlapping subproblems (that is, the repeated
calls). You then cache those results for future recursive calls.

Alternatively, you can study the patter of the recursive calls and implement
something iterative. You still "cache" previous work.

Let's start with an example. Fibonacci!

We can define fibonacci recursively as follows

```
def fibonacci(i: int) -> int:
	if i == 0:
		return 0
	if i == 1:
		return 1
	else:
		return fib(i - 1) + fib(i - 2)
```

What's the complexity of the above algorithm?

That's something we actually saw when talking about runtime calculation in 
the first chapter. The above runs in O(2^N) and takes O(N) memory.
Why?
Let's see with an example. i = 4
					fib(4) 
			fib(3) 			  fib(2)
		fib(2)	  	fib(1)	fib(1)	  fib(0)
  fib(1)  fib(0)   


So for i = 4 we have to compute 9 nodes in the above tree (the tree represents
the calls to each fibonacci call from its parent). The above looks like a binary tree :)
How many nodes do we have in a complete binary tree? 2^N where N equals the height. In this case
N = 4 => 2^4 = 16 is the max amount of nodes we can have, therefore the worst case complexity 
equals having the above tree complete, which is i, the input of our fibonacci method

*Note:* The thing to remember is that every time we see a recursive call in a method, that's a
branch that opens and it represents in the runtime complexity the base of our exponential factor. 
This means that we can have an N-tree where N equals the number of recursive calls. In the above
example, N = 2 => binary tree. 

*Note 2:* The memory is O(N) because it's the maximum recursive calls we can have in our stack 
for calculating one branch


Alright, one thing to take into consideration: The above fibonacci function it's calculating
a lot of times the same value! See the above tree and count the number of times we calculate 
fib(1) or fib(2) just for i = 4. Can we do better? Sure we can! What can we do? We can memoize
these values once they're calculated. Let's try to do that:


```
def fibonacci(i: int, precompute: list[int] = [0, 1]) -> int:
	"""
	We precompute the values of fibonacci and we take advantage
	on the fact that there's a unique precompute list created
	in the arity of the function
	"""
	if i < len(precompute):
		return precompute[i]
	elif i == len(precompute):
		precompute.append(precompute[i - 1] + precompute[i - 2])
		return precompute[i]
	else:
		prev = fibonacci(i - 1)
		precompute.append(precompute[i-1] + precompute[i-2])
		return precompute[i]
```


In the above code, we memoize values instead of having to re-calculate them every time :)

The above is considered top-down dynamic programming. Let's see the bottom-up dynamic programming approach :)

```
def fibonacci(i: int, precompute: list[int] = [0, 1]) -> int:
	if i < len(precompute):
		return precompute[i]
	
	k = len(precompute) # value to calculate
	while k != i + 1:
		precompute.append(precompute[k - 1] + precompute[k - 2])
		k += 1
	return precompute[i]

```

The big difference is that instead of recursively calling from "top" (the value we want to calculte) until "bottom"
(the values we need to do the calculation) we go the other way around: We calculate all "bottom" values until we reach
our top. We have transformed fibonacci in an iteratively function!


*Extra note*

If we don't want to memoize values of fibonacci because we know that we won't need them, we can iteratively 
calculate fibonacci as follows:
```
def fibonacci(i: int) -> int:
	if i == 0 or i == 1:
		return i
	a = 0
	b = 1
	c = a + b
	j = 2
	while j != i:
		c = a + b # new fib[j - 1] value
		a = b
		b = c
		j += 1
	return a + b
```
