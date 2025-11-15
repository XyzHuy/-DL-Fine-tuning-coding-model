import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        n = len(colors)
        
        # Check the distance between the first house and the last houses with different colors
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_distance = i
                break
        
        # Check the distance between the last house and the first houses with different colors
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_distance = max(max_distance, n - 1 - i)
                break
        
        return max_distance

def maxDistance(colors: List[int]) -> int:
    return Solution().maxDistance(colors)