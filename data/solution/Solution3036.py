import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def match(x: int, y: int, p: int) -> bool:
            if p == 1:
                return x < y
            elif p == 0:
                return x == y
            elif p == -1:
                return x > y
        
        count = 0
        n = len(nums)
        m = len(pattern)
        
        # Generate the pattern for nums
        nums_pattern = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                nums_pattern.append(1)
            elif nums[i] < nums[i - 1]:
                nums_pattern.append(-1)
            else:
                nums_pattern.append(0)
        
        # Use a sliding window to count matching subarrays
        for i in range(n - m):
            if all(match(nums[i + k], nums[i + k + 1], pattern[k]) for k in range(m)):
                count += 1
        
        return count

def countMatchingSubarrays(nums: List[int], pattern: List[int]) -> int:
    return Solution().countMatchingSubarrays(nums, pattern)