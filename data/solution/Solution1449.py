import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Dictionary to store the maximum number that can be formed with a given cost
        dp = {0: ""}
        
        # Iterate over each possible cost up to the target
        for t in range(1, target + 1):
            dp[t] = None
            for i in range(9):
                c = cost[i]
                if t >= c and dp[t - c] is not None:
                    candidate = str(i + 1) + dp[t - c]
                    if dp[t] is None or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate
        
        return dp[target] if dp[target] is not None else "0"

def largestNumber(cost: List[int], target: int) -> str:
    return Solution().largestNumber(cost, target)