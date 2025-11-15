import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        
        # dp[i] will be True if we can reach index i
        dp = [False] * n
        dp[0] = True
        reachable = 0  # number of reachable indices in the window [i-maxJump, i-minJump]
        
        for i in range(1, n):
            if i >= minJump:
                reachable += dp[i - minJump]
            if i > maxJump:
                reachable -= dp[i - maxJump - 1]
            if s[i] == '0' and reachable > 0:
                dp[i] = True
        
        return dp[-1]

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    return Solution().canReach(s, minJump, maxJump)