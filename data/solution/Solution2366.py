import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        
        # Start from the second last element and move to the first
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                # Calculate the number of parts we need to split nums[i] into
                parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                # The last number in the split should be as large as possible
                nums[i] = nums[i] // parts
                # Increment the number of operations by the number of splits minus one
                operations += parts - 1
        
        return operations

def minimumReplacement(nums: List[int]) -> int:
    return Solution().minimumReplacement(nums)