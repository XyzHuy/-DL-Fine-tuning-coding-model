import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a DP table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns with leading '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' can match zero or more of the preceding element
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or characters match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[len(s)][len(p)]

def isMatch(s: str, p: str) -> bool:
    return Solution().isMatch(s, p)