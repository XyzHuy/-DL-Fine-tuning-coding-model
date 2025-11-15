import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def manhattan_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        @lru_cache(None)
        def dp(worker_index, bike_mask):
            if worker_index == len(workers):
                return 0
            
            min_distance = float('inf')
            for bike_index in range(len(bikes)):
                if not (bike_mask & (1 << bike_index)):
                    distance = manhattan_distance(workers[worker_index], bikes[bike_index])
                    min_distance = min(min_distance, distance + dp(worker_index + 1, bike_mask | (1 << bike_index)))
            
            return min_distance
        
        return dp(0, 0)

def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> int:
    return Solution().assignBikes(workers, bikes)