import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        n = len(s)
        dp = [0] * (n + 1)
        
        for end in range(1, n + 1):
            dp[end] = dp[end - 1]  # Carry forward the maximum number of palindromes found so far
            
            # Check for palindromes of length k
            if end >= k and is_palindrome(s[end - k:end]):
                dp[end] = max(dp[end], dp[end - k] + 1)
            
            # Check for palindromes of length k + 1
            if end >= k + 1 and is_palindrome(s[end - k - 1:end]):
                dp[end] = max(dp[end], dp[end - k - 1] + 1)
        
        return dp[n]

def maxPalindromes(s: str, k: int) -> int:
    return Solution().maxPalindromes(s, k)