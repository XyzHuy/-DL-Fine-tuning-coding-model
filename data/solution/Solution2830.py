import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # Sort offers by end time
        offers.sort(key=lambda x: x[1])
        
        # Create a list of end times for binary search
        end_times = [offer[1] for offer in offers]
        
        # Initialize DP array
        dp = [0] * (len(offers) + 1)
        
        # Fill the DP array
        for i, (start, end, gold) in enumerate(offers, start=1):
            # Find the last offer that ends before the current offer starts
            j = bisect.bisect_right(end_times, start - 1)
            # Update dp[i] to be the maximum of taking this offer or not taking it
            dp[i] = max(dp[i - 1], dp[j] + gold)
        
        # The answer is the maximum gold that can be earned considering all offers
        return dp[len(offers)]

def maximizeTheProfit(n: int, offers: List[List[int]]) -> int:
    return Solution().maximizeTheProfit(n, offers)