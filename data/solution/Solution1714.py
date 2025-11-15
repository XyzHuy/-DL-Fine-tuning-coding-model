import random
import functools
import collections
import string
import math
import datetime


from typing import List

MOD = 10**9 + 7

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        max_y = max(y for _, y in queries)
        
        # Precompute prefix sums for each step size y
        prefix_sums = [None] * (max_y + 1)
        
        for y in range(1, max_y + 1):
            prefix_sums[y] = [0] * (n + 1)
            for x in range(n - 1, -1, -1):
                prefix_sums[y][x] = prefix_sums[y][min(x + y, n)] + nums[x]
                prefix_sums[y][x] %= MOD
        
        # Answer each query using the precomputed prefix sums
        result = []
        for x, y in queries:
            result.append(prefix_sums[y][x])
        
        return result

def solve(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().solve(nums, queries)