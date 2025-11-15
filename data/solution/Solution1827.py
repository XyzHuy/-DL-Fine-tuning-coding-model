import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed_increment = nums[i - 1] - nums[i] + 1
                operations += needed_increment
                nums[i] += needed_increment
        
        return operations

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)