import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # dp array to store the minimum cuts needed for the first i characters
        dp = [float('inf')] * n
        
        # Iterate over each character in the string
        for i in range(n):
            # Check for odd length palindromes centered at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1
            
            # Check for even length palindromes centered between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1
        
        return dp[n - 1]

def minCut(s: str) -> int:
    return Solution().minCut(s)