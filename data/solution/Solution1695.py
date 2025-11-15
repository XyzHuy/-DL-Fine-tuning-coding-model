import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        current_score = 0
        left = 0
        seen = set()
        
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_score -= nums[left]
                left += 1
            seen.add(nums[right])
            current_score += nums[right]
            max_score = max(max_score, current_score)
        
        return max_score

def maximumUniqueSubarray(nums: List[int]) -> int:
    return Solution().maximumUniqueSubarray(nums)