import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Edge cases
        if target == 0:
            return True
        if target > x + y:
            return False
        
        # The idea is to use the properties of the GCD (Greatest Common Divisor)
        # We can measure target liters if and only if target is a multiple of GCD(x, y)
        # and target is less than or equal to x + y
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return target % gcd(x, y) == 0

def canMeasureWater(x: int, y: int, target: int) -> bool:
    return Solution().canMeasureWater(x, y, target)