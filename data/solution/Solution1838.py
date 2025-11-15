import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] > total + k:
                total -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq

def maxFrequency(nums: List[int], k: int) -> int:
    return Solution().maxFrequency(nums, k)