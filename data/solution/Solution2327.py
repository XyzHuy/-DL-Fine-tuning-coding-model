import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        # dp[i] will store the number of people who know the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1  # On day 1, one person knows the secret
        
        for i in range(2, n + 1):
            # People who will start sharing the secret today
            for j in range(max(1, i - forget + 1), i - delay + 1):
                dp[i] = (dp[i] + dp[j]) % MOD
        
        # The result is the number of people who still remember the secret on day n
        return sum(dp[max(1, n - forget + 1):]) % MOD

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    return Solution().peopleAwareOfSecret(n, delay, forget)