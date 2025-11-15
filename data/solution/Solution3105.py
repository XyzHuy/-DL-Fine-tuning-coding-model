import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1
        current_length = 1
        last_direction = 0  # 0: undefined, 1: increasing, -1: decreasing
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if last_direction == 1:
                    current_length += 1
                else:
                    current_length = 2
                last_direction = 1
            elif nums[i] < nums[i - 1]:
                if last_direction == -1:
                    current_length += 1
                else:
                    current_length = 2
                last_direction = -1
            else:
                current_length = 1
                last_direction = 0
            
            max_length = max(max_length, current_length)
        
        return max_length

def longestMonotonicSubarray(nums: List[int]) -> int:
    return Solution().longestMonotonicSubarray(nums)