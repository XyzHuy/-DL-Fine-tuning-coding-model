import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            min_element = nums[i]
            max_element = nums[i]
            for j in range(i + 1, n):
                min_element = min(min_element, nums[j])
                max_element = max(max_element, nums[j])
                total_sum += max_element - min_element
        
        return total_sum

def subArrayRanges(nums: List[int]) -> int:
    return Solution().subArrayRanges(nums)