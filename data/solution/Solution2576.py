import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = (n + 1) // 2  # Start from the middle of the list
        marked_count = 0
        
        while left < right < n:
            if 2 * nums[left] <= nums[right]:
                marked_count += 2
                left += 1
                right += 1
            else:
                right += 1
        
        return marked_count

def maxNumOfMarkedIndices(nums: List[int]) -> int:
    return Solution().maxNumOfMarkedIndices(nums)