import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its right place if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        # Step 2: Find the first index where the number is not i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers are in the correct place, return n + 1
        return n + 1

def firstMissingPositive(nums: List[int]) -> int:
    return Solution().firstMissingPositive(nums)