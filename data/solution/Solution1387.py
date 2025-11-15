import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps
        
        # Create a list of tuples (power_value, number)
        power_values = [(power(x), x) for x in range(lo, hi + 1)]
        
        # Sort the list of tuples by power_value, then by number
        power_values.sort()
        
        # Return the k-th number in the sorted list
        return power_values[k - 1][1]

def getKth(lo: int, hi: int, k: int) -> int:
    return Solution().getKth(lo, hi, k)