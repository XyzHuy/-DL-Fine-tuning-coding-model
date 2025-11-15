import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create an array to store the maximum reach for each starting point
        max_reach = [0] * (n + 1)
        
        # Fill the max_reach array
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            max_reach[left] = max(max_reach[left], right)
        
        # Use a greedy algorithm to find the minimum number of taps
        taps = 0
        current_end = 0
        next_end = 0
        
        for i in range(n + 1):
            if i > next_end:
                return -1  # If we cannot reach this point, return -1
            if i > current_end:
                taps += 1
                current_end = next_end
            next_end = max(next_end, max_reach[i])
        
        return taps

def minTaps(n: int, ranges: List[int]) -> int:
    return Solution().minTaps(n, ranges)