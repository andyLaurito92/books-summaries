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


