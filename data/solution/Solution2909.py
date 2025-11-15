import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        # Precompute the minimum values to the left of each index
        left_min = [float('inf')] * n
        current_min = float('inf')
        for i in range(n):
            current_min = min(current_min, nums[i])
            left_min[i] = current_min
        
        # Precompute the minimum values to the right of each index
        right_min = [float('inf')] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            right_min[i] = current_min
        
        # Find the minimum sum of a mountain triplet
        min_sum = float('inf')
        for j in range(1, n - 1):
            if left_min[j] < nums[j] > right_min[j]:
                min_sum = min(min_sum, left_min[j] + nums[j] + right_min[j])
        
        return min_sum if min_sum != float('inf') else -1

def minimumSum(nums: List[int]) -> int:
    return Solution().minimumSum(nums)