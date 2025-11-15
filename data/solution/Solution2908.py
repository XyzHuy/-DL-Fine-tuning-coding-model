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
        min_sum = float('inf')
        found = False
        
        for j in range(1, n - 1):
            min_left = min(nums[i] for i in range(j))
            min_right = min(nums[k] for k in range(j + 1, n))
            
            if min_left < nums[j] > min_right:
                found = True
                min_sum = min(min_sum, min_left + nums[j] + min_right)
        
        return min_sum if found else -1

def minimumSum(nums: List[int]) -> int:
    return Solution().minimumSum(nums)