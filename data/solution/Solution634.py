import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 0:
            return 1
        if n == 1:
            return 0
        
        # Initialize base cases
        prev2 = 1  # D(0)
        prev1 = 0  # D(1)
        
        for i in range(2, n + 1):
            current = (i - 1) * (prev1 + prev2) % MOD
            prev2 = prev1
            prev1 = current
        
        return prev1

def findDerangement(n: int) -> int:
    return Solution().findDerangement(n)