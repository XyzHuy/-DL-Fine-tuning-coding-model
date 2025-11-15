import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(days), len(days[0])
        
        # Build a graph from flights
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    graph[i].append(j)
        
        # Add self-loops to allow staying in the same city
        for i in range(n):
            graph[i].append(i)
        
        # Initialize the dp array
        dp = [-1] * n
        dp[0] = 0
        
        # Iterate over each week
        for week in range(k):
            new_dp = [-1] * n
            for city in range(n):
                if dp[city] == -1:
                    continue
                for next_city in graph[city]:
                    new_dp[next_city] = max(new_dp[next_city], dp[city] + days[next_city][week])
            dp = new_dp
        
        return max(dp)

def maxVacationDays(flights: List[List[int]], days: List[List[int]]) -> int:
    return Solution().maxVacationDays(flights, days)