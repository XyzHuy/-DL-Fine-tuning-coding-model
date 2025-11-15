import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        def ways_one(c):
            if c == '*':
                return 9
            elif c == '0':
                return 0
            else:
                return 1
        
        def ways_two(c1, c2):
            if c1 == '*':
                if c2 == '*':
                    return 15  # 11-19, 21-26
                elif c2 in '0123456':
                    return 2  # 10-16, 20-26
                else:
                    return 1  # 17, 18, 19
            elif c1 == '1':
                if c2 == '*':
                    return 9  # 11-19
                else:
                    return 1
            elif c1 == '2':
                if c2 == '*':
                    return 6  # 21-26
                elif c2 in '0123456':
                    return 1
                else:
                    return 0
            else:
                return 0
        
        prev2 = 1  # dp[i-2]
        prev1 = ways_one(s[0])  # dp[i-1]
        
        for i in range(1, len(s)):
            current = 0
            current += prev1 * ways_one(s[i])
            current += prev2 * ways_two(s[i-1], s[i])
            current %= MOD
            prev2, prev1 = prev1, current
        
        return prev1

def numDecodings(s: str) -> int:
    return Solution().numDecodings(s)