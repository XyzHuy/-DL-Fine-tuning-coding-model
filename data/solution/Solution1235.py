import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the start time, end time, and profit into a single list of jobs
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        
        # Initialize dp array to store the maximum profit up to each job
        dp = [(0, 0)]  # (endTime, max_profit)
        
        for s, e, p in jobs:
            # Find the latest job that ends before the current job starts
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            
            # Calculate the maximum profit including the current job
            if dp[i][1] + p > dp[-1][1]:
                dp.append((e, dp[i][1] + p))
        
        # The last element in dp contains the maximum profit
        return dp[-1][1]

def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    return Solution().jobScheduling(startTime, endTime, profit)