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
	- We usually point bigger subproblems to smaller subproblems <--> a -> b iff a needs b in order to be solved.
- Base: cases of relation
- Original problem: solve via subproblems -> often is 1 of the subproblems
- Time analysis

The big idea of dynamic programming is memoization: Re-use the results of the different
subproblems to decrease the complexity of the solution!
Usually: Mantain a mapping such as mapping[subproblem] = res of subproblem

Then with the above, the subproblems either return a meoized solution or calculate it
and store it into a "memory"

*Note* Regarding running time: The time it takes *WITH MEMOIZATION* is 

*time <= sum subproblem_{i} * non-recursive work (this is, the work it takes to resolve each relation)*

Why the above time? Because subproblems are memoised! So that means that we should solve
each subproblem only 1 time. Therefore, sum subproblem_{i} represents that, the number of
subproblems we need to solve. Per each of these subproblems we have some non-recursive work to do (the work it takes the relation).

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
- prefixes x[:i] -> O(N) (there are a polinomial number of prefixes)
- suffixes x[i:] -> O(N) (there are a polinomial number of suffixes)
- substrings x[i:j] -> O(N^2) (for each i you have N N - 1 options => N * N - 1 = N^2 - N = N^2)

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


#### Example: Longest increasing subsequence

Given a string a, we want to find the longest increasing subsequence. This is, given 
CARBOHYDRATE -> ABORT (All leters are in increasing order and in their original order)


subproblem: lis(a) = lis(a[:i])
topological order: for i in range(n) where n = len(a)

relation:  Question to answer: Is a[i] in lis?

lis(a[:i]) = max(l(i+1), 1+l(i+1)) # Either a[i] belongs to the lis or it doesn't

There's a problem with the above definition: We are not enforcing a[i] to be less than 
it's next element. We could perfectly add the "if a[i] < a[i+1]", but this is WRONG! Why?
Because it's not always true that a[i+1] belongs to the longest increasing subsequence. The
only thing that we know is that a[i] might or might not belong to the longest increasing 
subsequence, and we know that it might exist j, where i < j <= len(a) - 1 where 
a[i] < a[j] (this is, j is the next character of the longest increasing subsequence). Our
problem right now is that we don't know where this j is and when it will occur!

So, how do we solve the above?

We change the subproblem definition! Instead of asking lis(a) = lis(a[:i]), we define
lis(a) = lis(a[:i]) where lis(a[:i]) ends with a[i] (is a[i] in lis(a)?). In other words:
Give me the longest increasing subsequence that ends up with a[i]

base case:
original problem:
time: 


### Alternating coin game

Given values of coins in sequence of values v0...vn-1, given 2 players, each player in each turn can either pick the first value or the last one. Once they pick a value, this is removed from the sequence, and then the next player repeats the process.
The goal of the game is to sum the highest score u can get

Example:

s = 5 10 100 25

Player 1: Can either choose 5 or 25. *Note* If player 1 chooses 25, because it's greater, then 
player 2 can choose 100! And with this they will win the game. Therefore, the smartest decision
for player 1 is to choose 5, so player 2 has to either choose 10 or 25 and finally player 1 
can choose 100 and win the game

subproblem: acg(s) = acg(s[i:j]) substrings
relation: acg(s[i:j]) = max(s[i]+acg(s[i+1:j]), s[j]+acg(s[i:j-1])
topological order: while i < j
base: n == 0 then 0 n == 1 then a[0]
original problem: acg(s[0:n-1])
runtime: O(N^2) (num of subproblems) * get the maximum = O(N^2)



*Personal note so far:* Building a recursive function and using memoization for 
solving dp doesn't seem to be that hard. The problem raises when u try 
to create a bottom up solution for the algorithm. Usually the problem comes 
on how to iterate on the data structure according to the problem you want
to solve.


### A bit of history

Dynamic programming was discovered by Bellman, the same guy as in Bellman & Ford algorithm for shortest path in 
a graph. 
The main idea of the programming technique is: Programming in that moment was also related to optimization, and
dynamic meant "We dynamically will get the best optimal answer". This goes against the "Statically get the best
solution from the "top""
