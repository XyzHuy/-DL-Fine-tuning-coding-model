import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = 0
        current_sum = 0
        element_count = Counter()
        
        # Initialize the first window
        for i in range(k):
            element_count[nums[i]] += 1
            current_sum += nums[i]
        
        # Check the first window
        if len(element_count) >= m:
            max_sum = current_sum
        
        # Slide the window over the array
        for i in range(k, len(nums)):
            # Add the new element to the window
            element_count[nums[i]] += 1
            current_sum += nums[i]
            
            # Remove the element that is no longer in the window
            element_count[nums[i - k]] -= 1
            current_sum -= nums[i - k]
            if element_count[nums[i - k]] == 0:
                del element_count[nums[i - k]]
            
            # Check if the current window is almost unique
            if len(element_count) >= m:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

def maxSum(nums: List[int], m: int, k: int) -> int:
    return Solution().maxSum(nums, m, k)