import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the numbers to handle duplicates easily
        result = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # Include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)
            
            # Exclude nums[i] from the subset
            subset.pop()
            
            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)
        
        dfs(0)
        return result

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    return Solution().subsetsWithDup(nums)