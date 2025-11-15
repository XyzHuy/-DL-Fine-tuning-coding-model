import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def is_beautiful(subset, num):
            for x in subset:
                if abs(x - num) == k:
                    return False
            return True

        def backtrack(index, current_subset):
            if index == len(nums):
                return 1 if current_subset else 0
            
            count = 0
            # Include nums[index] if it forms a beautiful subset
            if is_beautiful(current_subset, nums[index]):
                count += backtrack(index + 1, current_subset + [nums[index]])
            
            # Exclude nums[index]
            count += backtrack(index + 1, current_subset)
            
            return count
        
        return backtrack(0, [])

def beautifulSubsets(nums: List[int], k: int) -> int:
    return Solution().beautifulSubsets(nums, k)