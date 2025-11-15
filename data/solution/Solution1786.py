import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Create adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        
        # Dijkstra's algorithm to find shortest distance from each node to node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]  # (distance, node)
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > dist[u]:
                continue
            for v, weight in adj[u]:
                distance = current_dist + weight
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # Memoization to store the number of restricted paths from each node to node n
        memo = [-1] * (n + 1)
        
        def dfs(node):
            if node == n:
                return 1
            if memo[node] != -1:
                return memo[node]
            
            count = 0
            for neighbor, _ in adj[node]:
                if dist[node] > dist[neighbor]:
                    count = (count + dfs(neighbor)) % MOD
            
            memo[node] = count
            return count
        
        return dfs(1)

def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    return Solution().countRestrictedPaths(n, edges)