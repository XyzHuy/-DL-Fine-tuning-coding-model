import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}  # Initialize with difference 0 and height 0
        
        for rod in rods:
            new_dp = dp.copy()
            for d, h in dp.items():
                # Case 1: Do not use the rod
                # Case 2: Add the rod to the taller support
                new_dp[d + rod] = max(new_dp.get(d + rod, 0), h)
                # Case 3: Add the rod to the shorter support
                new_dp[abs(d - rod)] = max(new_dp.get(abs(d - rod), 0), h + min(d, rod))
            dp = new_dp
        
        return dp[0]  # The maximum height when both supports are equal

def tallestBillboard(rods: List[int]) -> int:
    return Solution().tallestBillboard(rods)