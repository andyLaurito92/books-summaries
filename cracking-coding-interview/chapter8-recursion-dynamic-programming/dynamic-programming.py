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

Given the count from right to left, this is taking prefixes, what we can ask ourselves is,
given the ith position, what should i do with it?
Subproblems: s(a[i:]) = max(s(a[i-1:]),
		a[i] + s(a[i-1:]),
		a[i-1] * a[i] + s(a[i-1:])
		)
Relate: Get the maximum
Topological order: for reversed(range(n, 1))
Base: [] = 0 and [v1] = max(v1, 0)
Original: s(a[0:])
Time: O(N)
Memory: O(N)

"""


"""
Python nomenclature for slicing:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
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
        

assert 110 == bowling([1, 1, 9, 9, 2, -5, -5])

assert 23 == bowling([3, 3, -2, 0, -1, 7, 2])
