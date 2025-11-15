import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # Calculate the minimum time to complete up to 15 consecutive laps with each tire
        best = [float('inf')] * 15
        for f, r in tires:
            total = 0
            for i in range(15):
                lap_time = f * (r ** i)
                total += lap_time
                if total >= 10**6:  # If the total time exceeds a large number, stop
                    break
                best[i] = min(best[i], total)
        
        # Initialize DP array
        dp = [float('inf')] * (numLaps + 1)
        dp[0] = 0
        
        # Fill the DP array
        for i in range(1, numLaps + 1):
            for j in range(min(15, i)):
                dp[i] = min(dp[i], dp[i - j - 1] + best[j] + changeTime)
        
        # The answer is dp[numLaps] - changeTime because we don't need to change tire after the last lap
        return dp[numLaps] - changeTime

def minimumFinishTime(tires: List[List[int]], changeTime: int, numLaps: int) -> int:
    return Solution().minimumFinishTime(tires, changeTime, numLaps)