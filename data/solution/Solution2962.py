import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_count = 0
        left = 0
        result = 0
        
        for right in range(len(nums)):
            if nums[right] == max_num:
                max_count += 1
            
            while max_count >= k:
                result += len(nums) - right
                if nums[left] == max_num:
                    max_count -= 1
                left += 1
        
        return result

def countSubarrays(nums: List[int], k: int) -> int:
    return Solution().countSubarrays(nums, k)