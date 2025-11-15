import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Helper function to check if all trips can be completed within given time t
        def canCompleteTrips(t):
            trips = 0
            for bus_time in time:
                trips += t // bus_time
            return trips >= totalTrips
        
        # Binary search for the minimum time
        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if canCompleteTrips(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def minimumTime(time: List[int], totalTrips: int) -> int:
    return Solution().minimumTime(time, totalTrips)