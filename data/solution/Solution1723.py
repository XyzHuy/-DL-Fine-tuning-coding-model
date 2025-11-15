import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        
        # Precompute the total time for each subset of jobs
        total_time = [0] * (1 << n)
        for mask in range(1 << n):
            for j in range(n):
                if mask & (1 << j):
                    total_time[mask] += jobs[j]
        
        @lru_cache(None)
        def dp(mask, workers):
            if workers == 1:
                return total_time[mask]
            res = float('inf')
            subset = mask
            while subset:
                res = min(res, max(total_time[subset], dp(mask ^ subset, workers - 1)))
                subset = (subset - 1) & mask
            return res
        
        return dp((1 << n) - 1, k)

def minimumTimeRequired(jobs: List[int], k: int) -> int:
    return Solution().minimumTimeRequired(jobs, k)