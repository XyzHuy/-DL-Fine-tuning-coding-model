import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # If the middle element is greater than the next element,
                # then the peak is in the left half (including mid)
                right = mid
            else:
                # If the middle element is less than or equal to the next element,
                # then the peak is in the right half (excluding mid)
                left = mid + 1
        
        # When left == right, we have found a peak element
        return left

def findPeakElement(nums: List[int]) -> int:
    return Solution().findPeakElement(nums)