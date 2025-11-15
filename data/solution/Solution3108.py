import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.min_cost = [0xFFFFFFFF] * n  # Initialize with all bits set to 1

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v, weight):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.min_cost[root_u] &= self.min_cost[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.min_cost[root_v] &= self.min_cost[root_u]
            else:
                self.parent[root_v] = root_u
                self.min_cost[root_u] &= self.min_cost[root_v]
                self.rank[root_u] += 1
        self.min_cost[root_u] &= weight
        self.min_cost[root_v] &= weight

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        
        # Union all edges
        for u, v, w in edges:
            uf.union(u, v, w)
        
        # Process each query
        result = []
        for s, t in query:
            if s == t:
                result.append(0)
            else:
                root_s = uf.find(s)
                root_t = uf.find(t)
                if root_s == root_t:
                    result.append(uf.min_cost[root_s])
                else:
                    result.append(-1)
        
        return result

def minimumCost(n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    return Solution().minimumCost(n, edges, query)