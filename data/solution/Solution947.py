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
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        
        # Create a dictionary to map x-coordinate and y-coordinate to stone indices
        x_coord = {}
        y_coord = {}
        
        for i, (x, y) in enumerate(stones):
            if x in x_coord:
                uf.union(i, x_coord[x])
            if y in y_coord:
                uf.union(i, y_coord[y])
            x_coord[x] = i
            y_coord[y] = i
        
        # The number of stones we can remove is total stones minus the number of connected components
        return n - uf.count

def removeStones(stones: List[List[int]]) -> int:
    return Solution().removeStones(stones)