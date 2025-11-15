import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import combinations

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0
        
        # Calculate the maximum possible bitwise OR of the entire array
        for num in nums:
            max_or |= num
        
        # Check all subsets
        for r in range(1, len(nums) + 1):
            for subset in combinations(nums, r):
                current_or = 0
                for num in subset:
                    current_or |= num
                if current_or == max_or:
                    count += 1
        
        return count

def countMaxOrSubsets(nums: List[int]) -> int:
    return Solution().countMaxOrSubsets(nums)