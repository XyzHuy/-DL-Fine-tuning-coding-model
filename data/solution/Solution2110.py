import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize the number of descent periods to the number of days (each day is a period of length 1)
        descent_periods = n
        
        # Length of the current descent period
        current_length = 1
        
        # Iterate through the prices to find descent periods
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                current_length += 1
            else:
                # If the current period ends, add the number of periods in this segment
                descent_periods += (current_length * (current_length - 1)) // 2
                current_length = 1
        
        # Add the descent periods from the last segment
        descent_periods += (current_length * (current_length - 1)) // 2
        
        return descent_periods

def getDescentPeriods(prices: List[int]) -> int:
    return Solution().getDescentPeriods(prices)