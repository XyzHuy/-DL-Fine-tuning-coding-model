import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calculate_cost(time_str, startAt):
            cost = 0
            current_digit = str(startAt)
            for digit in time_str:
                if digit != current_digit:
                    cost += moveCost
                    current_digit = digit
                cost += pushCost
            return cost
        
        # Calculate possible time representations
        times = []
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60
        
        # Case 1: Use minutes and seconds as is, if valid
        if 0 <= minutes <= 99:
            times.append(f"{minutes:02}{seconds:02}")
        
        # Case 2: Use minutes - 1 and seconds + 60, if valid
        if 0 <= minutes - 1 <= 99 and 0 <= seconds + 60 <= 99:
            times.append(f"{minutes - 1:02}{seconds + 60:02}")
        
        # Calculate the cost for each valid time representation
        min_cost = float('inf')
        for time_str in times:
            # Remove leading zeros for normalization
            normalized_time = time_str.lstrip('0') or '0'
            min_cost = min(min_cost, calculate_cost(normalized_time, startAt))
        
        return min_cost

def minCostSetTime(startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
    return Solution().minCostSetTime(startAt, moveCost, pushCost, targetSeconds)