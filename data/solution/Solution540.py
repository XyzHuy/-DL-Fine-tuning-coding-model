import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even for comparison with the next element
            if mid % 2 == 1:
                mid -= 1
            
            # If the element at mid is the same as the next element, the single element is in the right half
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                # Otherwise, the single element is in the left half
                right = mid
        
        # When left == right, we have found the single element
        return nums[left]

def singleNonDuplicate(nums: List[int]) -> int:
    return Solution().singleNonDuplicate(nums)