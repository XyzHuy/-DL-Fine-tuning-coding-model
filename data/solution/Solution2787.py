import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Generate all possible numbers that can be used (i^x <= n)
        max_base = 1
        while max_base**x <= n:
            max_base += 1
        max_base -= 1
        
        # Create a list of these numbers
        powers = [i**x for i in range(1, max_base + 1)]
        
        # Use dynamic programming to find the number of ways
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to make 0, which is using no numbers
        
        for power in powers:
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD
        
        return dp[n]

def numberOfWays(n: int, x: int) -> int:
    return Solution().numberOfWays(n, x)