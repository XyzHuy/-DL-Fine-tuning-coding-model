import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from functools import reduce

class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_gcd_sum = 0
        
        # Iterate over all possible starting points of the subarray
        for start in range(n - k + 1):
            current_gcd = nums[start]
            current_sum = nums[start]
            
            # Expand the window to at least k elements
            for end in range(start + 1, start + k):
                current_gcd = gcd(current_gcd, nums[end])
                current_sum += nums[end]
            
            # Calculate the gcd-sum for the current window of size k
            max_gcd_sum = max(max_gcd_sum, current_gcd * current_sum)
            
            # Continue expanding the window to the end of the array
            for end in range(start + k, n):
                current_gcd = gcd(current_gcd, nums[end])
                current_sum += nums[end]
                max_gcd_sum = max(max_gcd_sum, current_gcd * current_sum)
        
        return max_gcd_sum

def maxGcdSum(nums: List[int], k: int) -> int:
    return Solution().maxGcdSum(nums, k)