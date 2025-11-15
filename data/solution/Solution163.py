import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        def add_range(start, end):
            if start == end:
                missing_ranges.append([start, start])
            elif start < end:
                missing_ranges.append([start, end])
        
        missing_ranges = []
        prev = lower - 1
        
        for num in nums + [upper + 1]:
            if num > prev + 1:
                add_range(prev + 1, num - 1)
            prev = num
        
        return missing_ranges

# Example usage:
# sol = Solution()
# print(sol.findMissingRanges([0,1,3,50,75], 0, 99))  # Output: [[2,2],[4,49],[51,74],[76,99]]
# print(sol.findMissingRanges([-1], -1, -1))  # Output: []

def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    return Solution().findMissingRanges(nums, lower, upper)