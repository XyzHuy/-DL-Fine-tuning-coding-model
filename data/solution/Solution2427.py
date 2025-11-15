import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Find the minimum of a and b, as the common factors cannot be greater than the smaller number
        min_val = min(a, b)
        count = 0
        
        # Iterate through all numbers from 1 to min_val
        for x in range(1, min_val + 1):
            # Check if x is a factor of both a and b
            if a % x == 0 and b % x == 0:
                count += 1
        
        return count

def commonFactors(a: int, b: int) -> int:
    return Solution().commonFactors(a, b)