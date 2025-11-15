import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: empty string has one way to be split

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue  # Skip leading zeros
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > k:
                    break  # No need to check further if num exceeds k
                dp[i] = (dp[i] + dp[j + 1]) % MOD

        return dp[0]

def numberOfArrays(s: str, k: int) -> int:
    return Solution().numberOfArrays(s, k)