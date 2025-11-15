import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # Initialize the result with the last element of the array
        result = nums[-1]
        
        # Iterate from the second last element to the first element
        for i in range(len(nums) - 2, -1, -1):
            # If the current element can be combined with the next element
            if nums[i] <= result:
                result += nums[i]
            else:
                # Otherwise, update the result to the current element
                result = nums[i]
        
        return result

def maxArrayValue(nums: List[int]) -> int:
    return Solution().maxArrayValue(nums)