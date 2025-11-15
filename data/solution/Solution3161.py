import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = []
        results = []
        
        for query in queries:
            if query[0] == 1:
                # Add obstacle at position x
                bisect.insort(obstacles, query[1])
            elif query[0] == 2:
                x, sz = query[1], query[2]
                # Check if we can place a block of size sz in the range [0, x]
                can_place = False
                prev = 0
                idx = bisect.bisect_right(obstacles, x)
                for i in range(idx):
                    if obstacles[i] - prev >= sz:
                        can_place = True
                        break
                    prev = obstacles[i]
                if not can_place and x - prev >= sz:
                    can_place = True
                results.append(can_place)
        
        return results

def getResults(queries: List[List[int]]) -> List[bool]:
    return Solution().getResults(queries)