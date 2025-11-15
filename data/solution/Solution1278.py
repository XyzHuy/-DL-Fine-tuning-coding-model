import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        # Function to calculate the cost to make a substring s[start:end+1] a palindrome
        def cost(start, end):
            c = 0
            while start < end:
                if s[start] != s[end]:
                    c += 1
                start += 1
                end -= 1
            return c
        
        # DP table where dp[i][j] is the minimum cost to partition s[:i] into j palindromes
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost(p, i - 1))
        
        return dp[n][k]

def palindromePartition(s: str, k: int) -> int:
    return Solution().palindromePartition(s, k)