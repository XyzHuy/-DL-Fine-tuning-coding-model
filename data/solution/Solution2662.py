import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # Priority queue for Dijkstra's algorithm
        pq = [(0, start[0], start[1])]
        # Dictionary to store the minimum cost to reach each point
        min_cost = {(start[0], start[1]): 0}
        target = (target[0], target[1])
        
        # Add a special road from start to each special road's start point with the cost of Manhattan distance
        for x1, y1, x2, y2, cost in specialRoads:
            start_cost = abs(x1 - start[0]) + abs(y1 - start[1])
            if (x1, y1) not in min_cost or start_cost < min_cost[(x1, y1)]:
                min_cost[(x1, y1)] = start_cost
                heapq.heappush(pq, (start_cost, x1, y1))
        
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            
            # If we have reached the target, return the cost
            if (x, y) == target:
                return current_cost
            
            # Try to reach the target directly from the current position
            direct_cost = current_cost + abs(target[0] - x) + abs(target[1] - y)
            if target not in min_cost or direct_cost < min_cost[target]:
                min_cost[target] = direct_cost
                heapq.heappush(pq, (direct_cost, target[0], target[1]))
            
            # Try to use each special road from the current position
            for x1, y1, x2, y2, cost in specialRoads:
                if x1 == x and y1 == y:
                    new_cost = current_cost + cost
                    if (x2, y2) not in min_cost or new_cost < min_cost[(x2, y2)]:
                        min_cost[(x2, y2)] = new_cost
                        heapq.heappush(pq, (new_cost, x2, y2))
                else:
                    # Consider the cost of reaching the start of the special road
                    new_cost = current_cost + abs(x1 - x) + abs(y1 - y) + cost
                    if (x2, y2) not in min_cost or new_cost < min_cost[(x2, y2)]:
                        min_cost[(x2, y2)] = new_cost
                        heapq.heappush(pq, (new_cost, x2, y2))
        
        # The minimum cost to reach the target
        return min_cost[target]

def minimumCost(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    return Solution().minimumCost(start, target, specialRoads)