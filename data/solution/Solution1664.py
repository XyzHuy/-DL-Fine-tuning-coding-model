import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_sum = [0] * (n + 1)
        odd_sum = [0] * (n + 1)
        
        # Calculate prefix sums for even and odd indexed elements
        for i in range(n):
            if i % 2 == 0:
                even_sum[i + 1] = even_sum[i] + nums[i]
                odd_sum[i + 1] = odd_sum[i]
            else:
                odd_sum[i + 1] = odd_sum[i] + nums[i]
                even_sum[i + 1] = even_sum[i]
        
        count = 0
        
        # Check each index for fairness after removal
        for i in range(n):
            new_even_sum = even_sum[i] + (odd_sum[n] - odd_sum[i + 1])
            new_odd_sum = odd_sum[i] + (even_sum[n] - even_sum[i + 1])
            if new_even_sum == new_odd_sum:
                count += 1
        
        return count

def waysToMakeFair(nums: List[int]) -> int:
    return Solution().waysToMakeFair(nums)