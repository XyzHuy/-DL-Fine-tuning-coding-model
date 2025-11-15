import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # The score is defined by the sum of the first two elements
        target_score = nums[0] + nums[1]
        operations = 0
        
        # Iterate through the list in steps of 2
        i = 0
        while i + 1 < len(nums):
            if nums[i] + nums[i + 1] == target_score:
                operations += 1
            else:
                break
            i += 2
        
        return operations

def maxOperations(nums: List[int]) -> int:
    return Solution().maxOperations(nums)