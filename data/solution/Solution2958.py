import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            frequency[nums[right]] += 1
            
            while frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

def maxSubarrayLength(nums: List[int], k: int) -> int:
    return Solution().maxSubarrayLength(nums, k)