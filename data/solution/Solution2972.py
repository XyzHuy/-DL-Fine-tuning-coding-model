import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find the longest initial increasing subarray
        left = 0
        while left < n - 1 and nums[left] < nums[left + 1]:
            left += 1
        
        # If the entire array is strictly increasing
        if left == n - 1:
            return (n * (n + 1)) // 2
        
        # Find the longest final increasing subarray
        right = n - 1
        while right > 0 and nums[right] > nums[right - 1]:
            right -= 1
        
        # Count subarrays that lie entirely within the left part
        count = left + 1
        
        # Count subarrays that lie entirely within the right part
        count += n - right + 1
        
        # Count subarrays that span across the left and right parts
        i, j = 0, right
        while i <= left and j < n:
            if nums[i] < nums[j]:
                count += n - j
                i += 1
            else:
                j += 1
        
        return count

def incremovableSubarrayCount(nums: List[int]) -> int:
    return Solution().incremovableSubarrayCount(nums)