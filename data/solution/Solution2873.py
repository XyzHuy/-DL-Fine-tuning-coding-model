import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        n = len(nums)
        
        # Precompute the maximum values to the right of each index
        max_right = [0] * n
        max_right[-1] = nums[-1]
        for i in range(n - 2, 1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])
        
        max_left = nums[0]
        
        for j in range(1, n - 1):
            # Calculate the maximum value for the current j
            max_value = max(max_value, (max_left - nums[j]) * max_right[j + 1])
            # Update max_left for the next iteration
            max_left = max(max_left, nums[j])
        
        return max_value

def maximumTripletValue(nums: List[int]) -> int:
    return Solution().maximumTripletValue(nums)