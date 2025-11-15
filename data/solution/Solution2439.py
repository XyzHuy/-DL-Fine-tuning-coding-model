import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total_sum = 0
        max_val = 0
        
        for i, num in enumerate(nums):
            total_sum += num
            # Calculate the maximum value of the prefix average (ceiling of total_sum / (i + 1))
            max_val = max(max_val, math.ceil(total_sum / (i + 1)))
        
        return max_val

def minimizeArrayValue(nums: List[int]) -> int:
    return Solution().minimizeArrayValue(nums)