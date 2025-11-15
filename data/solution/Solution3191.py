import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        # Iterate through the array
        for i in range(n - 2):
            # If the current element is 0, we need to flip it and the next two elements
            if nums[i] == 0:
                # Perform the flip
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                # Increment the operation count
                operations += 1
        
        # Check if the last two elements are 1
        if nums[-2] != 1 or nums[-1] != 1:
            return -1
        
        return operations

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)