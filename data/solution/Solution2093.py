import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))
        
        # Priority queue to store (current_cost, city, remaining_discounts)
        pq = [(0, 0, discounts)]
        # Min cost to reach each city with a certain number of discounts used
        min_cost = [[float('inf')] * (discounts + 1) for _ in range(n)]
        min_cost[0][discounts] = 0
        
        while pq:
            current_cost, city, remaining_discounts = heapq.heappop(pq)
            
            # If we reach the destination city, return the current cost
            if city == n - 1:
                return current_cost
            
            # If the current cost is higher than the recorded minimum cost, skip
            if current_cost > min_cost[city][remaining_discounts]:
                continue
            
            # Explore neighbors
            for neighbor, toll in graph[city]:
                # Without using a discount
                new_cost = current_cost + toll
                if new_cost < min_cost[neighbor][remaining_discounts]:
                    min_cost[neighbor][remaining_discounts] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, remaining_discounts))
                
                # Using a discount
                if remaining_discounts > 0:
                    new_cost_discounted = current_cost + toll // 2
                    if new_cost_discounted < min_cost[neighbor][remaining_discounts - 1]:
                        min_cost[neighbor][remaining_discounts - 1] = new_cost_discounted
                        heapq.heappush(pq, (new_cost_discounted, neighbor, remaining_discounts - 1))
        
        # If we exhaust the priority queue without reaching the destination
        return -1

def minimumCost(n: int, highways: List[List[int]], discounts: int) -> int:
    return Solution().minimumCost(n, highways, discounts)