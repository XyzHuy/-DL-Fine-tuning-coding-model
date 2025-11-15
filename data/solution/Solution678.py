import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize two counters for the possible range of open parentheses
        low = 0  # Minimum number of open parentheses
        high = 0  # Maximum number of open parentheses
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1  # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
            # If high is negative, it means there are too many ')' at this point
            if high < 0:
                return False
            
            # low should never be negative, as we can't have less than 0 open parentheses
            low = max(low, 0)
        
        # In the end, low should be 0 to have a valid string
        return low == 0

def checkValidString(s: str) -> bool:
    return Solution().checkValidString(s)