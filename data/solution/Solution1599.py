import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        current_profit = 0
        max_rotation = -1
        waiting_customers = 0
        total_customers = 0
        rotations = 0
        
        for new_customers in customers:
            rotations += 1
            waiting_customers += new_customers
            boarding = min(4, waiting_customers)
            total_customers += boarding
            waiting_customers -= boarding
            current_profit += (boarding * boardingCost) - runningCost
            
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotation = rotations
        
        # Continue rotating if there are still waiting customers
        while waiting_customers > 0:
            rotations += 1
            boarding = min(4, waiting_customers)
            total_customers += boarding
            waiting_customers -= boarding
            current_profit += (boarding * boardingCost) - runningCost
            
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotation = rotations
        
        return max_rotation if max_profit > 0 else -1

def minOperationsMaxProfit(customers: List[int], boardingCost: int, runningCost: int) -> int:
    return Solution().minOperationsMaxProfit(customers, boardingCost, runningCost)