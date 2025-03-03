"""
Bowling: We are playing a new type of bowling :) Each pin has a value in it, and our goal is to maximize
our score. There are 3 possible actions per each pin:
- Hit it -> This adds vi to your score, where vi represents the value of the ith pin
- Don't hit it -> No addition to your current score
- Hit in the middle of 2 pins -> This adds the product of vi vj where vi, vj represent the value of pins i and j respectively

Given a list of integers which represent the values of each pin, our goal is to get the max score we can get from the given pins

Note: There can be negative values
"""


"""
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

"""


"""
Python nomenclature for slicing:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array -> sufixes
a[:stop]       # items from the beginning through stop-1 -> prefixes
a[:]           # a copy of the whole array
"""

def bowling(a: list[int]) -> int:
    def bowling_rec(a: list[int], memory: list[int] = [0]) -> int:
        """
        We start our memory with 0 because we use the lengths of the array as indexes.
        This implies that when n = 1 then we want a[1] to be the subproblem of s(a[1]). For doing
        this, we need to store in the memory s([]) which is always 0
        """
        n = len(a)
        if len(memory) > n:
            return memory[n]

        if n == 1:
            memory.append(max(0, a[0]))
            return memory[1]

        val = max(
             bowling_rec(a[:n-1]),
             a[n-1] + bowling_rec(a[:n-1]),
             a[n-2] * a[n-1] + bowling_rec(a[:n-2])
         )
        memory.append(val)
        return memory[n]
    return bowling_rec(a)
        

"""
Using bottom up dynamic programming technique to convert a recursive
algorithm in an iterative one
"""
def bowling2(a: list[int]) -> int:
    n = len(a)
    if n == 0:
        return 0
    elif n == 1:
        return max(a[0], 0)

    memory = [0, max(a[0], 0)]
    for i in range(2, n + 1):
        val = max(memory[i-1], a[i-1] + memory[i-1], a[i-1] * a[i-2] + memory[i-2])
        memory.append(val)
    return memory[n]
        


assert 110 == bowling([1, 1, 9, 9, 2, -5, -5])
assert 23 == bowling([3, 3, -2, 0, -1, 7, 2])
assert 0 == bowling([])
assert 5 == bowling([1, 1, 1, 1, 1])


assert 110 == bowling2([1, 1, 9, 9, 2, -5, -5])
assert 23 == bowling2([3, 3, -2, 0, -1, 7, 2])
assert 0 == bowling2([])
assert 5 == bowling2([1, 1, 1, 1, 1])
