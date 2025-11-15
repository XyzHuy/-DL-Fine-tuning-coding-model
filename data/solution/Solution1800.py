import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        # Final check to ensure the last subarray is considered
        max_sum = max(max_sum, current_sum)
        
        return max_sum

def maxAscendingSum(nums: List[int]) -> int:
    return Solution().maxAscendingSum(nums)