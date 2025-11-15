import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # Create the adjacency list for the graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        # Set to keep track of marked nodes for quick lookup
        marked_set = set(marked)
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, s)]
        # Dictionary to store the minimum distance to each node
        dist = {s: 0}
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # If the current distance is greater than the recorded distance, skip
            if current_dist > dist.get(u, float('inf')):
                continue
            
            # If u is a marked node, we can check if this is the minimum distance
            if u in marked_set:
                return current_dist
            
            # Explore neighbors
            for v, weight in graph[u]:
                distance = current_dist + weight
                if v not in dist or distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # If no path to any marked node is found, return -1
        return -1

def minimumDistance(n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
    return Solution().minimumDistance(n, edges, s, marked)