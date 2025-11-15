import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        max_length = 0
        n = len(nums)
        
        # Dictionary to store the first occurrence of each value
        first_occurrence = {}
        
        for i in range(n):
            # Update the first occurrence of nums[i]
            if nums[i] not in first_occurrence:
                first_occurrence[nums[i]] = i
            
            # Check all elements after the first occurrence of nums[i]
            for j in range(first_occurrence[nums[i]], n):
                if nums[i] > nums[j]:
                    max_length = max(max_length, j - first_occurrence[nums[i]] + 1)
        
        return max_length

def maxSubarrayLength(nums: List[int]) -> int:
    return Solution().maxSubarrayLength(nums)