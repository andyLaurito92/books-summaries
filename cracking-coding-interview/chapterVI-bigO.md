I like how the chapter starts making u reflect:

- You've got a file on a hard drive and u need to sent it to your friend who live across the country. U need to get
the file to your friend as fast as possible. How would u send it?

First most important question to ask (always!): What's the size of the input? :D (In this case, the file) ->

If the size is super big, then it might even make sense to physically transport the file! Even though the book
gives you an example of an airplane and a person, AWS provides such service via the [AWS Snowball Family](https://aws.amazon.com/snowball/)

The important thing to remember is this: 
1) When the transferred is done via an electronic way, the complexity of the transfer grows linearly (assumption) with the size
of the file
2) When the transferred is done phisically (somebody moves a hard drive via airplane to the destination), the complexity of the transfer
is always constant (doesn't matter how big the file it is, the plane will always take around the same time)

## Big O, Big Omega and Big Theta

*Note*: Remember that we care to measure in algorithms 2 things:
- Time: Which we measure by the number of operations an algorithm performs
- Memory: What is the amount of memory needed to perform the algorithm

Big O -> upper bound on the time. If the algorithm is printing all elements in a list, possible upper bounds are O(N), O(N^2), O(N^3) and so on
Big Omega -> lower bound on the time. Idem algorithm than above, possible lower bounds are O(N), O(log N), O(1)

Not very helpful :D What we are looking for in reality is

O big theta -> Means Big O and Big Omega at the same time. This is what we use in the industry as our standard =) (even though we call it Big O 
because we think in the "worst case")


*Goal*: To always offer the tighest description of the runtime


## Worst case, average case, best case

Measures to describe the runtime of our algorithm!

Best case: What's the best input that will make my algorithm perform in the fastest way

Worst case: What's the input that will make my algorithm perform in the worst way

Average case: What will be the average/most expected input of my algorithm and how will it perform in these situations?


*Note*: There's not particular relationship between worst/best/average case scenario and big o/big theta/big omega


## Example of space complexity

```
def sum(n: int) -> int:
	if n <= 0:
		return 0
	return n + sum(n - 1)
```

How much space does the above algorithm consume?

Each call to sum it's pushed into the stack, so we have for n = 3

sum(3)
 -> sum(2)
    -> sum(1)
	  -> 0
	  
So for N = 3, we had to push 3 calls into the stack + the final result. We can therefore induced that the space we need
is O(N) (Because we need N + 1 calls and +1 is constant, the factor that matters here is N). 

Note: The above algorithm also takes O(N) runtime! Remember that what it matters in runtime is the number of times we 
execute the different operations in the algorithm. In the above algorithm, we execute N + 1 checks for `n <= 0` and n + 1
sums, therefore the recursiveness doesn't add any value on decreasing the runtime and, on the contrary, augments the 
number of space I need to perform the operation

How can we do the above better? By iterating instead

```
def sum(n:int) -> int:
	accum = 0
	for i in range(n):
		accum += i
```

The algorithm now takes O(N) in runtime (as before), but now it takes O(1) in space memory


*Reminder*: We always drop the non-dominant time, meaning:

- O(N^2 + N) = O(N)
- O(N^3 + log(N)) = N^3

and so on. 

What we cannot do is drop a variable from the expression, for example: If you have A, B and
you're expressing the increase of complexity in runtime given these variables, then it means:
- O(A + B) remains like it is
- O(A^2 + A + log(B)) = O(A^2 + log(B)) bc what it matters is to reflect the increase given 
these 2 inputs


## Amortized time

The time you require for updating the underneath data structure for mantainance, such as a list in python 
implemented over an array and the action of having to resize the list because it has already reached
it's maximum. 

Given this time, which is allocating memory + copying all elements from the previous list to the new one +
adding the new element, we can estimate that every X time we will need to do O(N) for insertion.
However, this time is amortized by the constant time it takes in all the remaining times

If we assume that we always double the size of the array, then the num of operations we do in this worst case is
1 + 2 + 4 + 8 + 16 ... + X (so power of 2)
This can also be read as X + X/2 + X/4 ... + 1. What is the close sum of this series? 2X
Meaning that after X insertions, it will take O(2X)=O(X) time. This is the amortized time for each O(1) insertion


## Understanding log n runtimes

How logarithm runtines work? Let's take binary search as an example:

We have an array of N elements, we grab the middle elemnt, we do a comparisson and then we split 
the array of N elements to N/2 -> In this step, the num of operations is constant O(1)
Second step, same as above, and we divide the array again -> N/4
Third step, N/8
Fourth step, N/16
and so on until we either find the value or we are out of array (meaning that the dividend is greater than N)

How many times does the algorithm run? 

1 -> N/1 = N/2^(step - 1) # divide by 2
2 - > N/2 = N/2^(step - 1)# divide by 2
3 - > N/4= N/2^(step - 1)# divide by 2
4 -> N/8= N/2^(step - 1)# divide by 2

k -> N/K = N/2^(step - 1) -> 2^k-1

So basically we are looking for the first k that makes 2^k-1 >= N (because we know that we stop when we cannot
divide the array any longer)

*Note* Here k represents the number of iterations of the algorithm and is represented in relation with N, the size
of the array

So, to reply to the above question: What is the k that makes 2^k-1 >= N ==> log N = k, where N is a known value

*Remember*
2^4 = 16 => log 16 = 4
2^8 = 32 => log 32 = 8

a^k = N <=> log_a(N) = k

Log is the inverse of the exponential function and expreses the exponent you need to get to that value :) (in base 2
for our particular example because we live in a bit world)


*Take away* When you see a problem where in each iteration the number of elements in the
problem space gets halved each time, that will likely be an algorithm that takes O(log N) 
to run :)


## Recursive runtimes

What is the runtime of this code?

def f(n):
	return 1 if n <= 1 else f(n-1) + f(n-1)
	
	
Let's test with n=4
n= 4 => f(3) + f(3) # We call 2 times f(3)
n= 3 => f(2) + f(2) # We call 2 times f(2). Because we will call f(3) 2 times(in the above level), => 4 calls to f(2)
n=2 => f(1) + f(1) # Again, 2 times f(1) which will get called 8 times (2 per each node in the above level) -> Exponential patter
n=1 => 1 => Called 16 times

====

Remember that we are counting the number of times this algorithm executes according to the size of the input! This means, we need
to sum the above: 2^0=1 + 2^1=2 + 2^2=4 + 2^3=8 + 2^4=16 -> This would be the exact number of times the algorithm will run. 
The above sum, which can be depicted as sum(0, 4)2^i = 2^(4+1) - 1 => Our complexity is 2^(N+1) - 1. And as we saw above, 
we don't care about the constants factor because what we care about is giving an estimate of how fast the growth of execution
of this algorithm goes related to its input.

We can deduce from the above that we are creating a tree and the number of times this algorithm will run the if condition will be
2^4=16. So the branching here is giving us the base and the power is given by the length of the input.

Meaning, f runtime is O(2^N)

*Note*: if we add a new branch in f (where branch means add a new f(n-1), then we will be adding 1 to the base, i.e., the 
runtime complexity would increment to O(3^N)


*Note 2*: Why do we always say O(log N) and we don't really care about the base of the logarithm?

Answer -> Because the different bases are only different by a constant factor!! :D. This is the reason
why we don't care about the base of the algorithm
