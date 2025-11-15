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

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        
        # Calculate all edges with their weights (Manhattan distances)
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))
        
        # Sort edges based on their weights
        edges.sort()
        
        # Kruskal's algorithm to find the MST
        uf = UnionFind(n)
        mstCost = 0
        edgesUsed = 0
        
        for weight, u, v in edges:
            if uf.union(u, v):
                mstCost += weight
                edgesUsed += 1
                if edgesUsed == n - 1:
                    break
        
        return mstCost

def minCostConnectPoints(points: List[List[int]]) -> int:
    return Solution().minCostConnectPoints(points)