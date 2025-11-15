import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # Dictionary to store the count of each remainder and the minimum number with that remainder
        remainder_count = defaultdict(lambda: [0, float('inf')])
        
        # Populate the dictionary with the count and minimum number for each remainder
        for num in nums:
            remainder = num % space
            remainder_count[remainder][0] += 1
            remainder_count[remainder][1] = min(remainder_count[remainder][1], num)
        
        # Find the remainder with the maximum count
        # If there are multiple remainders with the same count, choose the one with the minimum number
        max_count = max(remainder_count.values(), key=lambda x: (x[0], -x[1]))
        
        # Return the minimum number that can destroy the maximum number of targets
        return max_count[1]

def destroyTargets(nums: List[int], space: int) -> int:
    return Solution().destroyTargets(nums, space)