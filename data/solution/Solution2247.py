import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))
        
        # If k is greater than or equal to n, it's impossible to visit each city at most once
        if k >= n:
            return -1
        
        # Use a recursive function with memoization to find the maximum cost
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(city, visited, remaining):
            if remaining == 0:
                return 0
            
            max_cost = -1
            for neighbor, toll in graph[city]:
                if not (visited & (1 << neighbor)):
                    cost = dfs(neighbor, visited | (1 << neighbor), remaining - 1)
                    if cost != -1:
                        max_cost = max(max_cost, cost + toll)
            
            return max_cost
        
        # Try starting from each city
        max_trip_cost = -1
        for start_city in range(n):
            cost = dfs(start_city, 1 << start_city, k)
            max_trip_cost = max(max_trip_cost, cost)
        
        return max_trip_cost

def maximumCost(n: int, highways: List[List[int]], k: int) -> int:
    return Solution().maximumCost(n, highways, k)