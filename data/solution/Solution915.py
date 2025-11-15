import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n
        
        # Fill max_left array
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        # Fill min_right array
        min_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        
        # Find the partition point
        for i in range(1, n):
            if max_left[i - 1] <= min_right[i]:
                return i
        
        return n  # This line should never be reached given the problem constraints

def partitionDisjoint(nums: List[int]) -> int:
    return Solution().partitionDisjoint(nums)