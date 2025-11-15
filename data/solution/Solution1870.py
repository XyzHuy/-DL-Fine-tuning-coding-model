import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        
        def can_arrive_on_time(speed: int) -> bool:
            total_time = 0.0
            for d in dist[:-1]:
                total_time += math.ceil(d / speed)
            total_time += dist[-1] / speed
            return total_time <= hour
        
        left, right = 1, 10**7
        while left < right:
            mid = (left + right) // 2
            if can_arrive_on_time(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def minSpeedOnTime(dist: List[int], hour: float) -> int:
    return Solution().minSpeedOnTime(dist, hour)