import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        total_count = 0
        start = 0
        
        for end in range(1, len(nums)):
            if nums[end] <= nums[end - 1]:
                # Calculate the number of subarrays in the range [start, end-1]
                length = end - start
                total_count += (length * (length + 1)) // 2
                start = end
        
        # Calculate the number of subarrays for the last increasing sequence
        length = len(nums) - start
        total_count += (length * (length + 1)) // 2
        
        return total_count

def countSubarrays(nums: List[int]) -> int:
    return Solution().countSubarrays(nums)