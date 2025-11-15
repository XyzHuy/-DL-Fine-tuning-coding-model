import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(max_distance):
            needed = 0
            for i in range(1, len(stations)):
                dist = stations[i] - stations[i - 1]
                needed += math.ceil(dist / max_distance) - 1
            return needed <= k
        
        left, right = 0.0, 10**8
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left

def minmaxGasDist(stations: List[int], k: int) -> float:
    return Solution().minmaxGasDist(stations, k)