import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # Dictionary to store prefix sums and their corresponding indices
        prefix_sums = {0: -1}
        current_sum = 0
        last_end = -1
        count = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # Check if there is a prefix sum that, when subtracted from current_sum, equals target
            if current_sum - target in prefix_sums and prefix_sums[current_sum - target] >= last_end:
                count += 1
                last_end = i
            
            # Store the current prefix sum with its index
            prefix_sums[current_sum] = i
        
        return count

def maxNonOverlapping(nums: List[int], target: int) -> int:
    return Solution().maxNonOverlapping(nums, target)