import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(types)
        
        # dp[i] will be the number of ways to get i points
        dp = [0] * (target + 1)
        dp[0] = 1  # There's one way to get 0 points: do nothing
        
        for count, marks in types:
            # Traverse the dp array backwards to avoid using the same type multiple times in one iteration
            for points in range(target, -1, -1):
                for solve in range(1, count + 1):
                    if points - solve * marks >= 0:
                        dp[points] = (dp[points] + dp[points - solve * marks]) % MOD
        
        return dp[target]

def waysToReachTarget(target: int, types: List[List[int]]) -> int:
    return Solution().waysToReachTarget(target, types)