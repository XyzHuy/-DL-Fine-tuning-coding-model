import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = []
        
        for i in range(n):
            prefix = nums[:i + 1]
            suffix = nums[i + 1:]
            distinct_prefix_count = len(set(prefix))
            distinct_suffix_count = len(set(suffix))
            diff.append(distinct_prefix_count - distinct_suffix_count)
        
        return diff

def distinctDifferenceArray(nums: List[int]) -> List[int]:
    return Solution().distinctDifferenceArray(nums)