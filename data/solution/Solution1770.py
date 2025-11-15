import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        
        @lru_cache(None)
        def dp(left, i):
            # If we have performed all m operations, return 0
            if i == m:
                return 0
            
            # Calculate the right index based on the left index and the current operation index
            right = n - 1 - (i - left)
            
            # Calculate the score if we pick the element from the left
            pick_left = multipliers[i] * nums[left] + dp(left + 1, i + 1)
            
            # Calculate the score if we pick the element from the right
            pick_right = multipliers[i] * nums[right] + dp(left, i + 1)
            
            # Return the maximum score of the two choices
            return max(pick_left, pick_right)
        
        # Start the recursion with the first element and the first operation
        return dp(0, 0)

def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    return Solution().maximumScore(nums, multipliers)