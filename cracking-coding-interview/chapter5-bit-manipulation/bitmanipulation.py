# Multiplying two numbers in binary
from collections import deque


def binary_rep(x: int, word_size: int = 8) -> list[int]:
    """
    Given a number, returns a list which represents the
    binary representation of this number in a word_size of
    8 bits. If the number is bigger than this, it will
    overflow

    TODO: What about negative numbers?
    """
    digits = deque()
    while x > 0:
        digits.appendleft(x % 2)
        x = int(x / 2)
        if len(digits) == word_size:
            # reached word_size
            return list(digits)

    while len(digits) != word_size:
        # Fill left digits w/0s
        digits.appendleft(0)

    return list(digits)


def shift_left(x: list[int], k :int) -> list[int]:
    """
    Shift x binary representation k to the left, filling w/0s
    right digits
    """
    n = len(x)
    for i in range(n - k):
        x[i] = x[i + k]
    for i in range(n - k, n):
        x[i] = 0
    return x


def to_decimal(x: list[int]) -> int:
    res = 0
    for i in range(len(x)):
        res += 2**x[0]
    return res


def binary_add(x: list[int], y: list[int], word_size: int = 8) -> list[int]:
    if len(x) != word_size or len(y) != word_size:
        raise ValueError("Binary is not of the expected word size")

    res = [0] * word_size
    carry = 0
    # least significant bit (LSB) is the right most operand, word_size = 8, pos = 7
    for i in reversed(range(len(x))):  # Both x and y have same word_size
        curr_sum = x[i] + y[i] + carry
        if curr_sum >= 2:
            carry = 1
        else:
            carry = 0
        res[i] = curr_sum % 2
    return res


def binary_mul(x: list[int], y: list[int], word_size: int = 8) -> list[int]:
    """
    Given 2 binary numbers, multiply them
    """
    res = [0] * word_size
    digit = 0
    for j in reversed(range(len(x))):
        if (x[j] == 1):
            res = binary_add(res, shift_left(y, digit), word_size)
        digit += 1
    return res
    

assert binary_rep(3) == [0, 0, 0, 0, 0, 0, 1, 1]
assert binary_rep(15) == [0, 0, 0, 0, 1, 1, 1, 1]

assert binary_add([0, 0, 1, 1], [0, 1, 0, 0], word_size=4) == [0, 1, 1, 1]
assert binary_add([0, 0, 1, 1], [0, 0, 0, 1], word_size=4) == [0, 1, 0, 0]

assert shift_left([0, 0, 1, 1], 2) == [1, 1, 0, 0]
assert shift_left([0, 0, 1, 1], 4) == [1, 0, 0, 0]
                  

#assert binary_rep(-3) == [0, 0, 0, 0, 1, 1, 1, 1]

assert binary_mul([0, 0, 1, 1], [0, 1, 0, 1], word_size=4) == [1, 1, 1, 1]
