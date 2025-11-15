import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp[i] will store the number of ways to decode the substring s[:i]
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Base case: empty string has one way to be decoded
        dp[1] = 1  # Base case: single non-zero digit can be decoded in one way
        
        for i in range(2, len(s) + 1):
            # Check if the current digit can form a valid single digit number
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Check if the previous two digits form a valid two digit number
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]

def numDecodings(s: str) -> int:
    return Solution().numDecodings(s)