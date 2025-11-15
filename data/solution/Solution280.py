import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True  # Start with the expectation of nums[0] <= nums[1]
        
        for i in range(len(nums) - 1):
            if less:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less = not less  # Toggle the expectation for the next pair

def wiggleSort(nums: List[int]) -> None:
    return Solution().wiggleSort(nums)