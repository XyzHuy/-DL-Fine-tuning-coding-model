import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from bisect import bisect_right
        
        # Sort events by start day
        events.sort()
        n = len(events)
        
        # DP array to store the maximum value obtainable for each event and each k
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Function to find the next non-overlapping event using binary search
        def find_next_event(idx):
            start_day = events[idx][1]
            return bisect_right(events, [start_day, float('inf'), float('inf')], lo=idx + 1)
        
        # Fill the DP table
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                # Option 1: Skip the current event
                skip_current = dp[i + 1][j]
                # Option 2: Take the current event and add its value to the best of the remaining events
                next_event = find_next_event(i)
                take_current = events[i][2] + dp[next_event][j - 1]
                # Choose the better option
                dp[i][j] = max(skip_current, take_current)
        
        # The answer is the maximum value obtainable by attending at most k events starting from the first event
        return dp[0][k]

def maxValue(events: List[List[int]], k: int) -> int:
    return Solution().maxValue(events, k)