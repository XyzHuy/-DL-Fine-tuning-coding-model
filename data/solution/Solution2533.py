import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (maxLength + 1)
        dp[0] = 1  # Base case: there's one way to have an empty string

        for i in range(1, maxLength + 1):
            if i - oneGroup >= 0:
                dp[i] = (dp[i] + dp[i - oneGroup]) % MOD
            if i - zeroGroup >= 0:
                dp[i] = (dp[i] + dp[i - zeroGroup]) % MOD

        # Sum up all the ways to form strings of length in the range [minLength, maxLength]
        return sum(dp[minLength:maxLength + 1]) % MOD

def goodBinaryStrings(minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
    return Solution().goodBinaryStrings(minLength, maxLength, oneGroup, zeroGroup)