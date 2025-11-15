import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        
        # Iterate over all possible starting points of subarrays
        for i in range(len(nums)):
            current_or = 0
            # Iterate over all possible ending points of subarrays starting from i
            for j in range(i, len(nums)):
                # Calculate the OR of the current subarray
                current_or |= nums[j]
                # Calculate the absolute difference and update min_diff if it's smaller
                min_diff = min(min_diff, abs(k - current_or))
                # If the current_or is already greater than or equal to k, no need to expand the subarray further
                if current_or >= k:
                    break
        
        return min_diff

def minimumDifference(nums: List[int], k: int) -> int:
    return Solution().minimumDifference(nums, k)