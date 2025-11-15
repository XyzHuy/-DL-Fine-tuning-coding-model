import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # Find the maximum element that can be the starting element of the largest subarray
        max_start_index = 0
        for i in range(len(nums) - k + 1):
            if nums[i] > nums[max_start_index]:
                max_start_index = i
        
        # Return the subarray starting from the index of the maximum element found
        return nums[max_start_index:max_start_index + k]

def largestSubarray(nums: List[int], k: int) -> List[int]:
    return Solution().largestSubarray(nums, k)