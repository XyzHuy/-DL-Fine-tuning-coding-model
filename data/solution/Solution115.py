import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] will store the number of distinct subsequences of s[:i] which equals t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # An empty t can be formed from any prefix of s by not selecting any characters.
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If the characters match, we can either include this character or not
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If the characters do not match, we can only exclude this character from s
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

def numDistinct(s: str, t: str) -> int:
    return Solution().numDistinct(s, t)