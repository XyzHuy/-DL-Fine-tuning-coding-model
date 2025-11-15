import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        
        # Build the graph
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # Priority queue to store (current cost, current time, current city)
        pq = [(passingFees[0], 0, 0)]
        # min_time_to_reach stores the minimum time to reach each city
        min_time_to_reach = [float('inf')] * n
        min_time_to_reach[0] = 0
        
        while pq:
            cost, time, city = heapq.heappop(pq)
            
            # If we reach the destination city within maxTime, return the cost
            if city == n - 1:
                return cost
            
            # Explore neighbors
            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time
                if new_time <= maxTime and new_time < min_time_to_reach[neighbor]:
                    min_time_to_reach[neighbor] = new_time
                    heapq.heappush(pq, (cost + passingFees[neighbor], new_time, neighbor))
        
        # If we cannot reach the destination city within maxTime, return -1
        return -1

def minCost(maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
    return Solution().minCost(maxTime, edges, passingFees)