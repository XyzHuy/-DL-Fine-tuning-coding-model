import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        zero_count = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    return Solution().findMaxConsecutiveOnes(nums)