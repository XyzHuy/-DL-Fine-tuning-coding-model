import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        count = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window if the score is not less than k
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
            count += right - left + 1
        
        return count

def countSubarrays(nums: List[int], k: int) -> int:
    return Solution().countSubarrays(nums, k)