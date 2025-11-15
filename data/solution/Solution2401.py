import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        current_and = 0
        max_length = 0
        
        for right in range(len(nums)):
            # While the current number nums[right] has a common bit with the current_and,
            # remove the leftmost number from the current window
            while current_and & nums[right] != 0:
                current_and ^= nums[left]
                left += 1
            
            # Include nums[right] in the current window
            current_and |= nums[right]
            # Update the maximum length of the nice subarray found so far
            max_length = max(max_length, right - left + 1)
        
        return max_length

def longestNiceSubarray(nums: List[int]) -> int:
    return Solution().longestNiceSubarray(nums)