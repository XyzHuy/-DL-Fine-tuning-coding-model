import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the slow pointer
        k = 0
        
        # Iterate with the fast pointer
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        
        # k is the index of the last unique element, so we return k + 1
        return k + 1

def removeDuplicates(nums: List[int]) -> int:
    return Solution().removeDuplicates(nums)