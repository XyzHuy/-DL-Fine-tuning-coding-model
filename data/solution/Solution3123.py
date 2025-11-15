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
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Dijkstra's algorithm to find shortest paths from 0 to all nodes
        def dijkstra(start, n):
            dist = [float('inf')] * n
            dist[start] = 0
            min_heap = [(0, start)]
            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d != dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(min_heap, (dist[v], v))
            return dist
        
        # Find shortest paths from 0 to all nodes
        dist_from_0 = dijkstra(0, n)
        # Find shortest paths from n-1 to all nodes
        dist_from_n_minus_1 = dijkstra(n - 1, n)
        
        # Step 4: Check each edge
        answer = [False] * len(edges)
        for i, (u, v, w) in enumerate(edges):
            if dist_from_0[u] + w + dist_from_n_minus_1[v] == dist_from_0[n - 1]:
                answer[i] = True
            elif dist_from_0[v] + w + dist_from_n_minus_1[u] == dist_from_0[n - 1]:
                answer[i] = True
        
        return answer

def findAnswer(n: int, edges: List[List[int]]) -> List[bool]:
    return Solution().findAnswer(n, edges)