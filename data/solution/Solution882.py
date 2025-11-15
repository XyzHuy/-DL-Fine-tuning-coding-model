import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
import collections

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Step 1: Build the graph
        graph = collections.defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))  # +1 for the original edge itself
            graph[v].append((u, cnt + 1))
        
        # Step 2: Dijkstra's algorithm to find shortest path from node 0
        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]  # (distance, node)
        
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        # Step 3: Count reachable nodes
        reachable = 0
        used = collections.defaultdict(int)
        
        # Count original nodes reachable within maxMoves
        for i in range(n):
            if distances[i] <= maxMoves:
                reachable += 1
        
        # Count reachable new nodes along each edge
        for u, v, cnt in edges:
            a = max(0, maxMoves - distances[u])
            b = max(0, maxMoves - distances[v])
            reachable += min(cnt, a + b)
        
        return reachable

def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    return Solution().reachableNodes(edges, maxMoves, n)