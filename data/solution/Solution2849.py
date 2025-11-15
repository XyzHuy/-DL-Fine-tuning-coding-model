import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Calculate the Chebyshev distance
        distance = max(abs(fx - sx), abs(fy - sy))
        
        # If the start and end points are the same
        if sx == fx and sy == fy:
            # If t is 1, we cannot stay in the same place for exactly 1 second
            return t != 1
        else:
            # Check if we can reach the destination in exactly t seconds
            return t >= distance

def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    return Solution().isReachableAtTime(sx, sy, fx, fy, t)