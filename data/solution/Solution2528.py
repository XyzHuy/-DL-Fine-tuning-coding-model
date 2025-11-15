import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import accumulate

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Calculate the initial power of each city
        initial_power = [0] * n
        prefix_sum = [0] + list(accumulate(stations))
        
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            initial_power[i] = prefix_sum[right + 1] - prefix_sum[left]
        
        # Binary search for the maximum possible minimum power
        def canAchieve(min_power):
            additional_stations = 0
            extra = [0] * (n + 1)
            current_power = 0
            
            for i in range(n):
                current_power += extra[i]
                if initial_power[i] + current_power < min_power:
                    needed = min_power - (initial_power[i] + current_power)
                    additional_stations += needed
                    if additional_stations > k:
                        return False
                    current_power += needed
                    if i + 2 * r + 1 < n:
                        extra[i + 2 * r + 1] -= needed
            
            return additional_stations <= k
        
        left, right = 0, max(initial_power) + k
        while left < right:
            mid = (left + right + 1) // 2
            if canAchieve(mid):
                left = mid
            else:
                right = mid - 1
        
        return left

def maxPower(stations: List[int], r: int, k: int) -> int:
    return Solution().maxPower(stations, r, k)