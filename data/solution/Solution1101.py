import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Sort the logs by timestamp
        logs.sort(key=lambda x: x[0])
        
        # Initialize union-find data structure
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Union by rank
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        # Number of connections
        connections = 0
        
        for timestamp, x, y in logs:
            if union(x, y):
                connections += 1
                # If we have n-1 connections, all are connected
                if connections == n - 1:
                    return timestamp
        
        return -1

def earliestAcq(logs: List[List[int]], n: int) -> int:
    return Solution().earliestAcq(logs, n)