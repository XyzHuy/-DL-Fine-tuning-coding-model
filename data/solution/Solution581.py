import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Create a sorted version of the array to compare with
        sorted_nums = sorted(nums)
        
        # Initialize variables to track the start and end of the subarray
        start = -1
        end = -2
        
        # Iterate through the array to find the first and last mismatch
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start == -1:
                    start = i
                end = i
        
        # The length of the subarray to be sorted
        return end - start + 1

def findUnsortedSubarray(nums: List[int]) -> int:
    return Solution().findUnsortedSubarray(nums)