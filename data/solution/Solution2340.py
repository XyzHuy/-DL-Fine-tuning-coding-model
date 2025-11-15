import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        # Find the index of the smallest element (leftmost occurrence)
        min_index = nums.index(min(nums))
        
        # Find the index of the largest element (rightmost occurrence)
        max_index = len(nums) - 1 - nums[::-1].index(max(nums))
        
        # Calculate the minimum swaps required
        swaps = min_index + (len(nums) - 1 - max_index)
        
        # If the smallest element is to the right of the largest element, we need to subtract one swap
        if min_index > max_index:
            swaps -= 1
        
        return swaps

def minimumSwaps(nums: List[int]) -> int:
    return Solution().minimumSwaps(nums)