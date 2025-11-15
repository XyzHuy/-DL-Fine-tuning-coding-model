import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)
            # Reset current_sum to zero if it becomes negative for max_sum calculation
            if current_sum < 0:
                current_sum = 0
        
        current_sum = 0
        
        for num in nums:
            current_sum += num
            # Reset current_sum to zero if it becomes positive for min_sum calculation
            if current_sum > 0:
                current_sum = 0
            min_sum = min(min_sum, current_sum)
        
        result = max(abs(max_sum), abs(min_sum))
        return result

def maxAbsoluteSum(nums: List[int]) -> int:
    return Solution().maxAbsoluteSum(nums)