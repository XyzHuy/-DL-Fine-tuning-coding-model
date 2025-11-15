import random
import functools
import collections
import string
import math
import datetime


import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair up capital and profits and sort by capital
        projects = list(zip(capital, profits))
        projects.sort()
        
        # Max-heap for profits (using negative values to simulate max-heap)
        max_heap = []
        i = 0
        n = len(projects)
        
        for _ in range(k):
            # Add all projects that can be started with current capital to the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If there are no projects we can start, break
            if not max_heap:
                break
            
            # Pop the most profitable project
            w += -heapq.heappop(max_heap)
        
        return w

def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    return Solution().findMaximizedCapital(k, w, profits, capital)