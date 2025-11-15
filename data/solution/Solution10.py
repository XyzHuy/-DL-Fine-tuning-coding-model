import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic programming table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[-1][-1] = True
        
        # Fill the table from bottom-right to top-left
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = (i < len(s)) and p[j] in {s[i], '.'}
                
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        
        return dp[0][0]

def isMatch(s: str, p: str) -> bool:
    return Solution().isMatch(s, p)