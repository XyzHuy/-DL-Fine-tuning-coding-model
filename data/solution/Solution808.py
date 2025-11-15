import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def soupServings(self, n: int) -> float:
        # For large n, the probability that A will be empty first approaches 1
        if n > 4800:
            return 1.0

        # Scale down the problem by dividing n by 25
        n = (n + 24) // 25  # This ensures we round up when n is not a multiple of 25

        # Memoization dictionary to store already computed probabilities
        memo = {}

        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            prob = (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3)) / 4
            memo[(a, b)] = prob
            return prob

        return dp(n, n)

def soupServings(n: int) -> float:
    return Solution().soupServings(n)