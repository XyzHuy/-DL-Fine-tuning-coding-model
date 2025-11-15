import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxNumber(self, n: int) -> int:
        # Find the highest power of 2 less than or equal to n
        highest_power_of_2 = 1
        while highest_power_of_2 <= n:
            highest_power_of_2 <<= 1
        highest_power_of_2 >>= 1
        
        # The result is the number just below the highest power of 2 greater than n
        return highest_power_of_2 - 1

# Explanation:
# The key observation is that the bitwise AND of a range of numbers will be zero
# if the range includes a transition from a number with a certain bit set to a number
# where that bit is not set. This transition typically happens when crossing a power of 2.
# For example, between 7 (0111) and 8 (1000). The highest number x such that the AND of [x, n] is zero
# is the highest power of 2 less than or equal to n, minus one.

def maxNumber(n: int) -> int:
    return Solution().maxNumber(n)