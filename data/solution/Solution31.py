import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If the entire array is decreasing, reverse it to get the smallest permutation
        if i == -1:
            nums.reverse()
            return
        
        # Find the element just larger than nums[i] to the right of i
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Swap the found elements
        nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the elements to the right of i to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])

def nextPermutation(nums: List[int]) -> None:
    return Solution().nextPermutation(nums)