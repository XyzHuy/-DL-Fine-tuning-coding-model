import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_position = min(steps, arrLen)  # You can't move further than the number of steps or the array length
        
        # dp[i] will be the number of ways to reach position i with the remaining steps
        dp = [0] * max_position
        dp[0] = 1  # There's one way to be at the start with 0 steps taken
        
        for _ in range(steps):
            new_dp = [0] * max_position
            for i in range(max_position):
                # Stay in the same place
                new_dp[i] = dp[i]
                # Move right if possible
                if i + 1 < max_position:
                    new_dp[i] = (new_dp[i] + dp[i + 1]) % MOD
                # Move left if possible
                if i - 1 >= 0:
                    new_dp[i] = (new_dp[i] + dp[i - 1]) % MOD
            dp = new_dp
        
        return dp[0]

def numWays(steps: int, arrLen: int) -> int:
    return Solution().numWays(steps, arrLen)