import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from functools import lru_cache
        
        total_sum = sum(nums)
        n = len(nums)
        MOD = 10**9 + 7
        
        # If total sum is less than 2*k, it's not possible to partition into two groups each with sum >= k
        if total_sum < 2 * k:
            return 0
        
        # dp[i][t] is the number of ways to make sum 't' using the first 'i' elements
        @lru_cache(None)
        def dp(i, t):
            if t < 0:
                return 0
            if i == 0:
                return 1 if t == 0 else 0
            return (dp(i - 1, t) + dp(i - 1, t - nums[i - 1])) % MOD
        
        # Total number of subsets
        total_subsets = (1 << n) % MOD
        
        # Number of subsets with sum < k
        invalid_subsets = 0
        for t in range(k):
            invalid_subsets += dp(n, t)
            invalid_subsets %= MOD
        
        # Each invalid subset corresponds to an invalid partition
        # We need to subtract these from the total number of partitions
        # Each subset can be paired with its complement, so we multiply by 2
        # But we need to subtract the invalid partitions twice (once for each subset in the pair)
        result = (total_subsets - 2 * invalid_subsets) % MOD
        
        return result

def countPartitions(nums: List[int], k: int) -> int:
    return Solution().countPartitions(nums, k)