import random
import functools
import collections
import string
import math
import datetime


from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        self.count -= 1
        return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Sort connections based on the cost
        connections.sort(key=lambda x: x[2])
        
        # Initialize Union-Find
        uf = UnionFind(n + 1)
        total_cost = 0
        edges_used = 0
        
        # Process each edge
        for u, v, cost in connections:
            if uf.union(u, v):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    return total_cost
        
        # If not all cities are connected, return -1
        return -1

def minimumCost(n: int, connections: List[List[int]]) -> int:
    return Solution().minimumCost(n, connections)