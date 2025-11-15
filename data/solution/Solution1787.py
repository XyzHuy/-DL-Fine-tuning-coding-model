import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = [defaultdict(int) for _ in range(k)]
        min_changes = [0] * k
        
        for i in range(n):
            freq[i % k][nums[i]] += 1
            min_changes[i % k] += 1
        
        dp = [0] + [float('inf')] * 1023
        for i in range(k):
            ndp = [min_changes[i] + min(dp)] * 1024
            for a, fa in freq[i].items():
                for x, fx in enumerate(dp):
                    ndp[a ^ x] = min(ndp[a ^ x], fx + min_changes[i] - fa)
            dp = ndp
        
        return dp[0]

def minChanges(nums: List[int], k: int) -> int:
    return Solution().minChanges(nums, k)