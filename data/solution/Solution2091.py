import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        # Find the indices of the minimum and maximum elements
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        
        # Ensure min_index is less than max_index for easier calculations
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        
        # Calculate the three possible ways to delete the elements
        # 1. Remove from the front up to the max_index + 1
        # 2. Remove from the back up to the len(nums) - min_index
        # 3. Remove from the front up to the min_index + 1 and from the back up to the len(nums) - max_index
        remove_from_front = max_index + 1
        remove_from_back = len(nums) - min_index
        remove_from_both_ends = (min_index + 1) + (len(nums) - max_index)
        
        # Return the minimum of the three options
        return min(remove_from_front, remove_from_back, remove_from_both_ends)

def minimumDeletions(nums: List[int]) -> int:
    return Solution().minimumDeletions(nums)