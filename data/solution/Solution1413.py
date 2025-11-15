import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Initialize the minimum start value to 1
        min_start_value = 1
        # Initialize the current step by step sum
        current_sum = 0
        
        # Iterate through the nums array
        for num in nums:
            # Update the current step by step sum
            current_sum += num
            # If the current step by step sum is less than 1,
            # we need to increase the start value
            if current_sum < 1:
                min_start_value = max(min_start_value, 1 - current_sum)
        
        return min_start_value

def minStartValue(nums: List[int]) -> int:
    return Solution().minStartValue(nums)