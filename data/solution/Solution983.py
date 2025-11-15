import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Initialize a DP array to store the minimum cost up to each day
        dp = [0] * (days[-1] + 1)
        
        # Convert days list to a set for O(1) lookups
        travel_days = set(days)
        
        # Iterate over each day from 1 to the last travel day
        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                # If it's not a travel day, the cost is the same as the previous day
                dp[day] = dp[day - 1]
            else:
                # If it's a travel day, consider buying a 1-day, 7-day, or 30-day pass
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )
        
        # The last element in dp array is the minimum cost to cover all travel days
        return dp[days[-1]]

def mincostTickets(days: List[int], costs: List[int]) -> int:
    return Solution().mincostTickets(days, costs)