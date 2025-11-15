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
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Create two halves
        mid = (len(nums) + 1) // 2
        first_half = nums[:mid]
        second_half = nums[mid:]
        
        # Step 3: Reverse both halves
        first_half.reverse()
        second_half.reverse()
        
        # Step 4: Interleave the elements
        idx = 0
        while first_half or second_half:
            if first_half:
                nums[idx] = first_half.pop()
                idx += 1
            if second_half:
                nums[idx] = second_half.pop()
                idx += 1

def wiggleSort(nums: List[int]) -> None:
    return Solution().wiggleSort(nums)