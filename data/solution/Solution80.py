import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        k = 2  # Initialize the position to place the next valid element
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        
        return k

def removeDuplicates(nums: List[int]) -> int:
    return Solution().removeDuplicates(nums)