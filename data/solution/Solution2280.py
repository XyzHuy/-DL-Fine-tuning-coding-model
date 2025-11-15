import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        
        # Sort the stock prices by day (x-axis)
        stockPrices.sort()
        
        # Initialize the number of lines needed
        num_lines = 0
        prev_slope_numerator = None
        prev_slope_denominator = None
        
        # Iterate through the sorted stock prices
        for i in range(1, len(stockPrices)):
            # Calculate the slope between the current point and the previous point
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            slope_numerator = y2 - y1
            slope_denominator = x2 - x1
            
            # Check if the slope has changed
            if (prev_slope_numerator is None or 
                prev_slope_denominator is None or 
                slope_numerator * prev_slope_denominator != slope_denominator * prev_slope_numerator):
                num_lines += 1
                prev_slope_numerator = slope_numerator
                prev_slope_denominator = slope_denominator
        
        return num_lines

def minimumLines(stockPrices: List[List[int]]) -> int:
    return Solution().minimumLines(stockPrices)