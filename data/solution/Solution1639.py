import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)
        
        # Count the frequency of each character at each position in words
        char_count = [defaultdict(int) for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][char] += 1
        
        # dp[i][j] represents the number of ways to form target[0:j] using words[0:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: There's one way to form an empty target
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Don't use the current column (i-1) in words
                dp[i][j] = dp[i-1][j]
                
                # Case 2: Use the current column (i-1) in words if possible
                if char_count[i-1][target[j-1]] > 0:
                    dp[i][j] += dp[i-1][j-1] * char_count[i-1][target[j-1]]
                    dp[i][j] %= MOD
        
        return dp[m][n]

def numWays(words: List[str], target: str) -> int:
    return Solution().numWays(words, target)