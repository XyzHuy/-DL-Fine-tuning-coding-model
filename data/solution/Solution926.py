import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Initialize counters for flips and number of ones encountered
        flips = 0
        ones_count = 0
        
        # Iterate through the binary string
        for char in s:
            if char == '1':
                # Increment the count of ones
                ones_count += 1
            else:
                # When we encounter a '0', we have two choices:
                # 1. Flip this '0' to '1'
                # 2. Flip all previous '1's to '0's
                # We take the minimum of these two choices
                flips = min(flips + 1, ones_count)
        
        return flips

def minFlipsMonoIncr(s: str) -> int:
    return Solution().minFlipsMonoIncr(s)