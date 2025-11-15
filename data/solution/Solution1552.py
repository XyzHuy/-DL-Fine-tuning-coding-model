import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions to make it easier to calculate distances
        position.sort()
        
        def canPlaceBalls(min_distance: int) -> bool:
            # Place the first ball in the first basket
            count = 1
            last_position = position[0]
            
            # Try to place the remaining balls
            for i in range(1, len(position)):
                if position[i] - last_position >= min_distance:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        # Binary search for the maximum minimum distance
        low, high = 1, position[-1] - position[0]
        best_distance = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                best_distance = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best_distance

def maxDistance(position: List[int], m: int) -> int:
    return Solution().maxDistance(position, m)