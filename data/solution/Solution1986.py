import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import combinations

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        # Precompute all possible subsets and their total times
        subset_times = [0] * (1 << n)
        for i in range(n):
            for mask in range(1 << i):
                subset_times[mask | (1 << i)] = subset_times[mask] + tasks[i]
        
        # Initialize the DP table
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        # Try to find the minimum number of sessions
        for mask in range(1 << n):
            subset = mask
            while subset:
                if subset_times[subset] <= sessionTime:
                    dp[mask] = min(dp[mask], dp[mask ^ subset] + 1)
                subset = (subset - 1) & mask
        
        return dp[(1 << n) - 1]

def minSessions(tasks: List[int], sessionTime: int) -> int:
    return Solution().minSessions(tasks, sessionTime)