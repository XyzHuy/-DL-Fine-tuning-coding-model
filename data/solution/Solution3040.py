import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, j, score):
            if i >= j:
                return 0
            if i == j - 1:
                return 1 if nums[i] + nums[j] == score else 0
            
            max_ops = 0
            if nums[i] + nums[i + 1] == score:
                max_ops = max(max_ops, 1 + dp(i + 2, j, score))
            if nums[j] + nums[j - 1] == score:
                max_ops = max(max_ops, 1 + dp(i, j - 2, score))
            if nums[i] + nums[j] == score:
                max_ops = max(max_ops, 1 + dp(i + 1, j - 1, score))
            
            return max_ops
        
        n = len(nums)
        if n < 2:
            return 0
        
        # Try starting with the first two elements
        score1 = nums[0] + nums[1]
        # Try starting with the last two elements
        score2 = nums[n - 1] + nums[n - 2]
        # Try starting with the first and the last elements
        score3 = nums[0] + nums[n - 1]
        
        return max(dp(0, n - 1, score1), dp(0, n - 1, score2), dp(0, n - 1, score3))

def maxOperations(nums: List[int]) -> int:
    return Solution().maxOperations(nums)