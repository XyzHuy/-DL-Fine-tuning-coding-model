import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        n = len(nums)
        quotient, remainder = divmod(target, total_sum)
        
        # If the remainder is 0, we can directly return the quotient * n
        if remainder == 0:
            return quotient * n
        
        # We need to find the shortest subarray with sum equal to the remainder
        # We will use a sliding window approach to find this subarray
        min_length = float('inf')
        current_sum = 0
        left = 0
        
        # Extend nums to handle the infinite nature by considering it twice
        extended_nums = nums + nums
        
        for right in range(len(extended_nums)):
            current_sum += extended_nums[right]
            
            while current_sum > remainder:
                current_sum -= extended_nums[left]
                left += 1
            
            if current_sum == remainder:
                min_length = min(min_length, right - left + 1)
        
        # If we found a valid subarray, return its length plus the full cycles
        if min_length != float('inf'):
            return min_length + quotient * n
        
        return -1

def minSizeSubarray(nums: List[int], target: int) -> int:
    return Solution().minSizeSubarray(nums, target)