import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_difference = -1
        
        for num in nums[1:]:
            if num > min_value:
                max_difference = max(max_difference, num - min_value)
            else:
                min_value = num
        
        return max_difference

def maximumDifference(nums: List[int]) -> int:
    return Solution().maximumDifference(nums)