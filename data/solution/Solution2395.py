import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = set()
        
        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            if current_sum in seen_sums:
                return True
            seen_sums.add(current_sum)
        
        return False

def findSubarrays(nums: List[int]) -> bool:
    return Solution().findSubarrays(nums)