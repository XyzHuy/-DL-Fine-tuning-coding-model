import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False
        
        # Calculate prefix sums
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        # Try every possible j
        for j in range(3, n - 3):
            seen_sums = set()
            # Try every possible i
            for i in range(1, j - 1):
                if prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]:
                    seen_sums.add(prefix_sum[i - 1])
            # Try every possible k
            for k in range(j + 2, n - 1):
                if prefix_sum[n - 1] - prefix_sum[k] == prefix_sum[k - 1] - prefix_sum[j] and prefix_sum[k - 1] - prefix_sum[j] in seen_sums:
                    return True
        
        return False

def splitArray(nums: List[int]) -> bool:
    return Solution().splitArray(nums)