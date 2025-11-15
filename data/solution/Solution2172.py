import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dfs(index, slots):
            if index == len(nums):
                return 0
            
            max_and_sum = 0
            slots_list = list(slots)
            
            for slot in range(numSlots):
                if slots_list[slot] > 0:
                    # Place nums[index] in slot+1
                    slots_list[slot] -= 1
                    current_and_sum = (nums[index] & (slot + 1)) + dfs(index + 1, tuple(slots_list))
                    max_and_sum = max(max_and_sum, current_and_sum)
                    # Backtrack
                    slots_list[slot] += 1
            
            return max_and_sum
        
        # Initialize slots with 2 for each slot
        initial_slots = tuple([2] * numSlots)
        return dfs(0, initial_slots)

def maximumANDSum(nums: List[int], numSlots: int) -> int:
    return Solution().maximumANDSum(nums, numSlots)