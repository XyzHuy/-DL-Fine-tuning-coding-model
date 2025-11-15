import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = -1
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                current_length = 2
                j = i + 2
                while j < n and nums[j] == nums[j - 2]:
                    current_length += 1
                    j += 1
                max_length = max(max_length, current_length)
        
        return max_length if max_length > 1 else -1

def alternatingSubarray(nums: List[int]) -> int:
    return Solution().alternatingSubarray(nums)