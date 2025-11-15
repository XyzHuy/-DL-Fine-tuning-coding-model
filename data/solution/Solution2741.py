import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @cache
        def dp(mask, last):
            if mask == (1 << n) - 1:
                return 1
            count = 0
            for j in range(n):
                if not mask & (1 << j) and (nums[last] % nums[j] == 0 or nums[j] % nums[last] == 0):
                    count = (count + dp(mask | (1 << j), j)) % MOD
            return count
        
        total = 0
        for i in range(n):
            total = (total + dp(1 << i, i)) % MOD
        
        return total

def specialPerm(nums: List[int]) -> int:
    return Solution().specialPerm(nums)