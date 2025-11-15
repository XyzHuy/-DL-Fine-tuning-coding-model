import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        min_diff = float('inf')
        min_index = -1
        
        for i in range(n):
            left_sum += nums[i]
            left_avg = left_sum // (i + 1)
            
            right_sum = total_sum - left_sum
            if i < n - 1:
                right_avg = right_sum // (n - i - 1)
            else:
                right_avg = 0
            
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                min_index = i
        
        return min_index

def minimumAverageDifference(nums: List[int]) -> int:
    return Solution().minimumAverageDifference(nums)