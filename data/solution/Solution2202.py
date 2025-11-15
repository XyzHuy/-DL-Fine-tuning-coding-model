import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # If there's only one element and k is odd, we'll end up with an empty pile
        if n == 1 and k % 2 == 1:
            return -1
        
        # If k is 0, the topmost element remains the same
        if k == 0:
            return nums[0]
        
        # If k is 1, we can only remove the top element
        if k == 1:
            return nums[1] if n > 1 else -1
        
        # Consider the maximum value we can get by removing up to k-1 elements
        # and then placing the largest of the removed elements back on top
        max_value = max(nums[:k-1], default=-1)
        
        # Also consider the element that will be on top after k removals
        if k < n:
            max_value = max(max_value, nums[k])
        
        return max_value

def maximumTop(nums: List[int], k: int) -> int:
    return Solution().maximumTop(nums, k)