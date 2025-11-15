import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the base cases
        a, b = 1, 2
        
        # Compute the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            a, b = b, a + b
        
        return b

def climbStairs(n: int) -> int:
    return Solution().climbStairs(n)