import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than the rightmost element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than the rightmost element, the minimum is in the left half including mid
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element is equal to the rightmost element, we cannot determine the side, reduce the search space
            else:
                right -= 1
        
        return nums[left]

def findMin(nums: List[int]) -> int:
    return Solution().findMin(nums)