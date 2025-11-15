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
        self.size = 1  # Number of nodes in the single connected component

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            # Union by rank
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            self.size += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Initialize Union-Find for Alice and Bob
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        
        used_edges = 0
        
        # First, use all type 3 edges
        for edge in edges:
            if edge[0] == 3:
                if uf_alice.union(edge[1] - 1, edge[2] - 1):
                    uf_bob.union(edge[1] - 1, edge[2] - 1)
                    used_edges += 1
        
        # Then, use type 1 and type 2 edges
        for edge in edges:
            if edge[0] == 1:
                if uf_alice.union(edge[1] - 1, edge[2] - 1):
                    used_edges += 1
            elif edge[0] == 2:
                if uf_bob.union(edge[1] - 1, edge[2] - 1):
                    used_edges += 1
        
        # Check if Alice and Bob can fully traverse the graph
        if uf_alice.size != n or uf_bob.size != n:
            return -1
        
        # The number of removable edges is the total number of edges minus the number of edges used
        return len(edges) - used_edges

def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    return Solution().maxNumEdgesToRemove(n, edges)