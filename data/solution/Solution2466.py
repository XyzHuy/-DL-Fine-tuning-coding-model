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
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: there's one way to have a string of length 0, which is the empty string
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        
        # Sum up all the ways to form strings of length between low and high
        return sum(dp[low:high + 1]) % MOD

def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    return Solution().countGoodStrings(low, high, zero, one)