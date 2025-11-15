import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        # Initialize the direction of the first wiggle
        up = None
        max_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if up is False or up is None:
                    up = True
                    max_length += 1
            elif nums[i] < nums[i - 1]:
                if up is True or up is None:
                    up = False
                    max_length += 1
        
        return max_length

def wiggleMaxLength(nums: List[int]) -> int:
    return Solution().wiggleMaxLength(nums)