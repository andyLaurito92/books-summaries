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



"""
Longest common subsequence (LCS)
Given 2 sequences a, b, find the longest common subsequence
between them

Note:
- Substring is a sequence that has to be consecutive
- Subsequence is a sequence that doesn't necessarily needs to be consecutive. This means, if we have a = MICHAELANGELO then MAELGO is a valid subsequence :). You can have blanks in between, you can skip items

Example:
Given a = HIEROGLYPHOLOGY and b = MICHAELANGELO the LCS=HELLO :) (There might be more than 1 longest common subsequence)
"""

"""
Let's apply STRBOT

Example: SOMEAJFHEQNOVX, SXOMEAJ
		    	    ''
		  S    	               '' 			S
	        SX     S              X	''			X
	     SXO    SX    SO S      XO X O   ''			O
	  SXOM SXO SXM SX SOM SO SM S XOM XO XM X OM O M ''	M

subproblem: What if we use prefixes for only one of the given strings?
Then, we fix a and what we want to ask is: What is the lcs between a
and b[:i] s(a, b[:i]) = max(len(s(a, b[:i-1]) + b[i]), b[i]) is a
subsequence then s(a, b[:i-1] + b[i] else s(a, b[:i-1]) topological
order: for i in range(1, len(b)) relation between subproblems: Given
s(a, b[:i-1]) lcs, add b[i] and find out if it's still subsequence
Base case: if len(a) == 0 or len(b) == 0 then return '' original
problem: s(a, b[:n]) where len(b) = n time: depends on how much time
it takes to validate that s(a, b[:i-1]) + b[i] is a subsequence. If we
use a map we can do this in average constant time, worst case
O(len(b)).  Then => O(len(b) * len(a))

"""

from collections import defaultdict

def issubsequence(a:str, b:str) -> bool:
    """
    Determine if b is subsequence of a
    """
    if len(b) > len(a):
        return False

    mapping = defaultdict(list)
    for k, letter in enumerate(a):
        mapping[letter].append(k)

    i_a = 0
    for j, letter in enumerate(b):
        idxes = mapping.get(letter, None)
        if idxes is None:
            return False
        else:
            k = 0
            while k < len(idxes) and i_a > idxes[k]:
                k += 1

            if k >= len(idxes) or idxes[k] < i_a:
                return False
            
            i_a = idxes[k]
            mapping[letter] = idxes[k+1:]
            if len(mapping[letter]) == 0:
                del mapping[letter]
    return True
        

"""
The trick here is to generate valid subsequences in an optimal way. For this, we use
memoization to "not having to generate everything again from scratch"

Subproblem would be: s(a, b[:i]) = 

"""

def longestcommonsubsequence_backtracking(a: str, b:str) -> str:
    if len(b) == 0:
        return ''

    memory = [{''}]
    lcs = ''
    for i in range(len(b)):
        curr = set()
        curr.add('')
        if issubsequence(a, b[i]):
            curr.add(b[i])
        for x in memory[i]:
            subs = x + b[i]
            if issubsequence(a, subs):
                curr.add(subs)
                if len(subs) > len(lcs):
                    lcs = subs
        memory.append(curr.union(memory[i]))
    return lcs


"""
subproblem, s(i, j) = lcs(a[i], b[j]) # So subproblem is how you define your subproblems. This usually means using prefixes, sufixes, how you iterate over the inputs
topological order: for i in range(len(a)) for j in range(len(b))
relation:  s(a[i], b[j]) if a[i] == b[j]: 1 + s(a[i+1:], b[j+1:]) else max(s(a[i+1:], b[j:]), s(a[i:], b[j+1:])
base case: if len(a) == 0 or len(b) == 0 return 0
original problem: s(a[n], b[m]) where n = len(a) & m = len(b)
time: sum subproblems * non-recursive work => O(N^2) is the num of subproblems * O(1) (taking
max and if condition) => O(N^2)
"""
def longestcommonsubsequence(a: str, b:str) -> int:
    if len(a) == 0 or len(b) == 0:
        return 0

    n = len(a)
    m = len(b)
    memory = []
    # We fill up the memory with 0 values
    for i in range(n+1): # 0 = empty string, 1 = len(a) == 1. It's not the idxes
        memory.append([])
        for _ in range(m+1):
            memory[i].append((0, (0, 0)))

    
    for i in range(1, n+1):
        for j in range(1, m+1):
            parent_pointer = (i-1, j-1)
            if a[i-1] == b[j-1]:
                val = 1 + memory[i-1][j-1][0]
            else:
                if memory[i-1][j] > memory[i][j-1]:
                    val = memory[i-1][j][0]
                    parent_pointer = (i-1, j)
                else:
                    val = memory[i][j-1][0]
                    parent_pointer = (i, j-1)
            memory[i][j] = (val, parent_pointer)

    # find the lcs
    lcs = []
    i, j = (n, m)
    while i != 0 and j != 0:
        nextpair = memory[i][j][1]
        if (i-1, j-1) == nextpair:
            lcs.insert(0, a[i-1])
        i, j = nextpair
        

    res = ''.join(lcs)
    return res
                


assert "HEGLO" == longestcommonsubsequence_backtracking('HIEROGLYPHOLOGY', 'MICHAELANGELO')
assert "I" == longestcommonsubsequence_backtracking('SOMETHINGFUN', 'I')
assert "MJ" == longestcommonsubsequence_backtracking('SOMETHINGFUNJEJE', 'MJ')
assert "SOME" == longestcommonsubsequence_backtracking('SOMETHINGFUNJEJEX', 'SXOME')
assert "HABBCDFK" == longestcommonsubsequence_backtracking('HABBCDFKUNCJ', 'HJABBCDFK')


assert "IELLO" == longestcommonsubsequence('HIEROGLYPHOLOGY', 'MICHAELANGELO')
assert "I" == longestcommonsubsequence('SOMETHINGFUN', 'I')
assert "MJ" == longestcommonsubsequence('SOMETHINGFUNJEJE', 'MJ')
assert "SOME" == longestcommonsubsequence('SOMETHINGFUNJEJEX', 'SXOME')
assert "HABBCDFK" == longestcommonsubsequence('HABBCDFKUNCJ', 'HJABBCDFK')



"""
subproblem: substrings, a[i:j]
topological order: for i in range(n) for j in range(i, n)
relation: s(a, i, j) = if a[j] > s(a, i, j-1)[j-2] then a[j] + s(a, i, j+1) else max(s(a, i, j+1), s(a, i+1, j))
base case: s(a, 0, 0) = ''
original problem: s(a, n, n)
time: if len(a) = N then O(N^2) * constant time (solve non-recursive problem) => O(N^2)
"""

"""
CARBOHYDRATE
			''
		C		'' 			C
	   CA	     A	     A 		''		A

CARB
C -> C
CA -> C|A
CAR -> AR
CARB -> AR|AB
"""

def longestincreasingsubsequence(a: str) -> str:
    """
    Given a string a, return the longest increasing subsequence
    """

    n = len(a)
    if n == 0:
        return ''

    lis = ''
    memory = []
    for i in range(n):
        memory.apepnd([])
        for _ in range(i, n):
            memory[i].append('')
    
    lis = []
    # CARB
    # lis=[],i = 0, j = 1, memory=[['', '', '', ''], ['', '', ''], ['', ''], ['']]
    # len_subs = 0, subs = '', if C > ''
    for i in range(n):
        for j in range(i, n):
            len_subs = len(memory[i][j-1])
            subs = memory[i][j-1]
            if a[j] > subs[len_subs-1]:
                val = subs.append(a[j])
            else:
                val = subs
            memory[i][j] = val
            if len(lis) < len(val):
                lis = val

    return ''.join(lis)
