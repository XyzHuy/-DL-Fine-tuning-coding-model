import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # dp[i][j] will be the number of valid permutations of length i+1
        # ending with the j-th smallest number.
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Base case: There is one way to arrange a sequence of length 1
        for j in range(n + 1):
            dp[0][j] = 1
        
        # Fill the dp table
        for i in range(1, n + 1):
            if s[i - 1] == 'D':
                # If we need a decreasing sequence, we sum all valid permutations
                # of length i that end with a number greater than the current number
                total = 0
                for j in range(n - i + 1):
                    total = (total + dp[i - 1][j]) % MOD
                    dp[i][j] = total
            else:
                # If we need an increasing sequence, we sum all valid permutations
                # of length i that end with a number less than the current number
                total = 0
                for j in range(n - i + 1, -1, -1):
                    dp[i][j] = total
                    total = (total + dp[i - 1][j]) % MOD
        
        # The result is the sum of all valid permutations of length n+1
        return sum(dp[n]) % MOD

def numPermsDISequence(s: str) -> int:
    return Solution().numPermsDISequence(s)