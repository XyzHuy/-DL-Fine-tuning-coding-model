import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff < -2**31 or diff > 2**31 - 1:
                    continue
                dp[i][diff] += dp[j][diff] + 1
                count += dp[j][diff]
        
        return count

def numberOfArithmeticSlices(nums: List[int]) -> int:
    return Solution().numberOfArithmeticSlices(nums)