import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def twoEggDrop(self, n: int) -> int:
        # The problem can be solved using the mathematical insight that we need to find the smallest x
        # such that x * (x + 1) / 2 >= n. This is because we start from the x-th floor, then (x-1)-th floor,
        # and so on, which gives us a sum of the first x natural numbers.
        
        # We can solve this using a simple loop to find the smallest x.
        moves = 0
        while n > 0:
            moves += 1
            n -= moves
        return moves

def twoEggDrop(n: int) -> int:
    return Solution().twoEggDrop(n)