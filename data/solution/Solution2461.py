import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        element_count = defaultdict(int)
        
        for i in range(len(nums)):
            # Add the current element to the window
            current_sum += nums[i]
            element_count[nums[i]] += 1
            
            # Remove the element that is left out of the window
            if i >= k:
                current_sum -= nums[i - k]
                element_count[nums[i - k]] -= 1
                if element_count[nums[i - k]] == 0:
                    del element_count[nums[i - k]]
            
            # Check if the current window is valid
            if len(element_count) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

def maximumSubarraySum(nums: List[int], k: int) -> int:
    return Solution().maximumSubarraySum(nums, k)