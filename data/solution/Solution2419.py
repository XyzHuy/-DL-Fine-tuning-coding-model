import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find the maximum value in the array
        max_value = max(nums)
        
        # Initialize variables to track the length of the longest subarray
        max_length = 0
        current_length = 0
        
        # Iterate through the array to find the longest subarray with the maximum value
        for num in nums:
            if num == max_value:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
        
        return max_length

def longestSubarray(nums: List[int]) -> int:
    return Solution().longestSubarray(nums)