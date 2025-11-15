import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Create a list of tuples (value, index) and sort it by value
        indexed_nums = sorted((num, idx) for idx, num in enumerate(nums))
        
        # Initialize the maximum width and the minimum index
        max_width = 0
        min_index = float('inf')
        
        # Iterate through the sorted list to find the maximum width ramp
        for num, idx in indexed_nums:
            max_width = max(max_width, idx - min_index)
            min_index = min(min_index, idx)
        
        return max_width

def maxWidthRamp(nums: List[int]) -> int:
    return Solution().maxWidthRamp(nums)