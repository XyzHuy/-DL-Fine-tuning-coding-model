import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Calculate F(0)
        F = sum(i * nums[i] for i in range(n))
        total_sum = sum(nums)
        
        # Initialize the maximum value with F(0)
        max_value = F
        
        # Calculate F(k) for k from 1 to n-1
        for k in range(1, n):
            F = F + total_sum - n * nums[n-k]
            max_value = max(max_value, F)
        
        return max_value

def maxRotateFunction(nums: List[int]) -> int:
    return Solution().maxRotateFunction(nums)