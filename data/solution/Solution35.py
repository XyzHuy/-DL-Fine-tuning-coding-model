import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

def searchInsert(nums: List[int], target: int) -> int:
    return Solution().searchInsert(nums, target)