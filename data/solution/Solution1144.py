import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        moves_even = 0
        moves_odd = 0
        
        for i in range(n):
            if i % 2 == 0:
                # For even index, compare with neighbors
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < n - 1 else float('inf')
                target = min(left, right) - 1
                if nums[i] > target:
                    moves_even += nums[i] - target
            else:
                # For odd index, compare with neighbors
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < n - 1 else float('inf')
                target = min(left, right) - 1
                if nums[i] > target:
                    moves_odd += nums[i] - target
        
        return min(moves_even, moves_odd)

def movesToMakeZigzag(nums: List[int]) -> int:
    return Solution().movesToMakeZigzag(nums)