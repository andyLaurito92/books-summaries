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


The book doesn't go much further than this. MIT course to take a look at: https://www.youtube.com/watch?v=r4-cftqTcdI


## Dynamic Programming from MIT course

### Design Paradigm for Dynamic Programming (think of divide & conquer)

Let's define the following algorithm design paradigm: SRTBOT

- Subproblem: Definition of the subproblems --> This is the hardest part usually
	- Ideally we want a polinomial number of it
- Relate: Subproblem solution recursively
- Topological order on subproblems to guarantee acyclig DAG -> vertices = subproblems; edges -> order in which we need to solve the subproblems. Usually just a for loop
- Base: cases of relation
- Original problem: solve via subproblems -> often is 1 of the subproblems
- Time analysis

The big idea of dynamic programming is memoization: Re-use the results of the different
subproblems to decrease the complexity of the solution!
Usually: Mantain a mapping such as mapping[subproblem] = res of subproblem

Then with the above, the subproblems either return a meoized solution or calculate it
and store it into a "memory"

*Note* Regarding running time: The time it takes *WITH MEMOIZATION* is 

*time <= sum subproblem_{i} non-recursive work (this is, the work it takes to resolve each relation)*

Why the above time? Because subproblems are memoised! So that should take O(1)

Important note: If we don't use memoization the running time is exponential!

Once you've reduced your problem to the above algorithm design paradigm, you just need to
apply this framework:

```
def f(subproblem):
	if subproblem in memo:
		return memo[subproblem]
		
	if subproblem is base:
		base
	else:
		recursive via relation
```

#### Example 1: Bowling

Bowling: We are playing a new type of bowling :) Each pin has a value in it, and our goal is to maximize
our score. There are 3 possible actions per each pin:
- Hit it -> This adds vi to your score, where vi represents the value of the ith pin
- Don't hit it -> No addition to your current score
- Hit in the middle of 2 pins -> This adds the product of vi vj where vi, vj represent the value of pins i and j respectively

Given a list of integers which represent the values of each pin, our goal is to get the max score we can get from the given pins

Note: There can be negative values

Let's use our design paradigm for dynamic programming

What are the subproblems we want to solve?

Given the count from left to right, this is taking prefixes, what we can ask
ourselves is, given the ith position, what's the max possible score I can get
startint with pins i, i +1 ... n-1

Subproblems: max score s(a[:i]) = max(s(a[:i-1]),
		a[i] + s(a[:i-1]),
		a[i-1] * a[i] + s(a[:i-2])
		)
How many subproblems do I have? O(N)! Because it's prefixes
Relate (Can I write a recurrence relation?): s(i) = max(s(i-1), a[i] + s(i-1), a[i] * a[i-1] + s(i-2))
Topological order: Increasing order (prefixes) for range(2, n)
Base: n == 0 => res= 0 and n == 1 => [v1] = max(v1, 0)
Original: s(a[0:])
Time: O(N) * O(1) where O(1) is the non-recursive work I need to do for solving each subproblem
Memory: O(N)

### Tricks

Subproblem design: If input is a sequence, then good subproblems are:
- prefixes x[:i]
- suffixes x[i:]
- substrings x[i:j]

### Bottom up DP
For the bowling subproblem 

```
s(0) = 0  # base
for i=range(2, n) # topological order
	s(i) = max(s(i-1), a[i] + s(i-1), a[i-1] * a[i-2] + s(i-2)) # relate
return s(n) # orginal problem

```

#### Example: Mergesort

- Subproblems: s(i, j) = sorted array on a[i:j]
- relate: s(i,j) = merge(s(i, m), s(m, j)), m = i + [(j - 1) / 2]
- Topo order: increasing j - i
- base case: s(i, i) = []
- original problem: s(0, n)
- Time: T(n) = 2T(n/2) + O(N) = O(N lg N)

