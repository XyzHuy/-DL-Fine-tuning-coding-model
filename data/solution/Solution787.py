import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Min-heap to store (cost, current city, number of stops)
        min_heap = [(0, src, -1)]  # (cost, city, stops)
        visited = [False] * n
        
        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)
            
            # If we reach the destination, return the cost
            if city == dst:
                return cost
            
            # If the number of stops exceeds k, continue to the next iteration
            if stops == k:
                continue
            
            # Explore the neighbors of the current city
            for neighbor, price in graph[city]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops + 1))
        
        # If we exhaust the heap without finding a valid path, return -1
        return -1

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    return Solution().findCheapestPrice(n, flights, src, dst, k)