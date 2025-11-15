import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        def dijkstra(start: int) -> List[int]:
            distances = [float('inf')] * n
            distances[start] = 0
            min_heap = [(0, start)]
            while min_heap:
                current_dist, current_city = heapq.heappop(min_heap)
                if current_dist > distances[current_city]:
                    continue
                for neighbor, weight in adj[current_city]:
                    distance = current_dist + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))
            return distances
        
        min_reachable_cities = n
        city_with_min_reachable = -1
        
        for city in range(n):
            distances = dijkstra(city)
            reachable_cities = sum(1 for d in distances if d <= distanceThreshold)
            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                city_with_min_reachable = city
        
        return city_with_min_reachable

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    return Solution().findTheCity(n, edges, distanceThreshold)