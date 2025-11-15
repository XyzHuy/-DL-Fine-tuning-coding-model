import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if Koko can eat all bananas at speed k within h hours
        def canFinish(k: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            return hours_needed <= h
        
        # Binary search for the minimum eating speed
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid - 1  # Try a smaller speed
            else:
                left = mid + 1   # Need a larger speed
        
        return left  # left will be the minimum speed that works

def minEatingSpeed(piles: List[int], h: int) -> int:
    return Solution().minEatingSpeed(piles, h)