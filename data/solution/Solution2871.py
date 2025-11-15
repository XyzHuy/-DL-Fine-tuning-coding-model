import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        # Calculate the overall AND of the entire array
        overall_and = nums[0]
        for num in nums:
            overall_and &= num
        
        # If the overall AND is not zero, we can only have one subarray
        if overall_and != 0:
            return 1
        
        # Otherwise, we need to find the maximum number of subarrays with AND 0
        current_and = -1  # Start with all bits set to 1
        count = 0
        
        for num in nums:
            current_and &= num
            if current_and == 0:
                count += 1
                current_and = -1  # Reset current_and for the next subarray
        
        return count

def maxSubarrays(nums: List[int]) -> int:
    return Solution().maxSubarrays(nums)