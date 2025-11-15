import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            current_load = 0
            day_count = 1  # Start with the first day
            
            for weight in weights:
                if weight > capacity:
                    return False  # A single package is too heavy for the ship
                if current_load + weight > capacity:
                    day_count += 1
                    current_load = weight
                else:
                    current_load += weight
            
            return day_count <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def shipWithinDays(weights: List[int], days: int) -> int:
    return Solution().shipWithinDays(weights, days)