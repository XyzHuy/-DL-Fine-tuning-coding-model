import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for the current element, the boundary of 0s, and the boundary of 2s
        low, mid, high = 0, 0, len(nums) - 1
        
        # One-pass algorithm to sort the array in-place
        while mid <= high:
            if nums[mid] == 0:
                # Swap the current element with the element at the low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move to the next element
                mid += 1
            else:
                # Swap the current element with the element at the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

def sortColors(nums: List[int]) -> None:
    return Solution().sortColors(nums)