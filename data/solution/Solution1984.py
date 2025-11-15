import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # If k is 1, the minimum difference is always 0 because we pick the same student twice
        if k == 1:
            return 0
        
        # Sort the nums array to make it easier to find the minimum difference
        nums.sort()
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        
        # Use a sliding window of size k to find the minimum difference
        for i in range(len(nums) - k + 1):
            # Calculate the difference between the highest and lowest scores in the current window
            diff = nums[i + k - 1] - nums[i]
            # Update the minimum difference if the current difference is smaller
            min_diff = min(min_diff, diff)
        
        return min_diff

def minimumDifference(nums: List[int], k: int) -> int:
    return Solution().minimumDifference(nums, k)