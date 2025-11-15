import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
                self.size[rootU] += self.size[rootV]
    
    def getSize(self, u):
        return self.size[self.find(u)]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Create a copy of the grid with all hits applied
        copy_grid = [row[:] for row in grid]
        for i, j in hits:
            copy_grid[i][j] = 0
        
        # Union-Find data structure
        uf = UnionFind(m * n + 1)  # +1 for the virtual top node
        top = m * n
        
        # Helper function to convert 2D coordinates to 1D
        def getIndex(i, j):
            return i * n + j
        
        # Connect all stable bricks to the virtual top node and to each other
        for j in range(n):
            if copy_grid[0][j] == 1:
                uf.union(getIndex(0, j), top)
        
        for i in range(m):
            for j in range(n):
                if copy_grid[i][j] == 1:
                    for dx, dy in DIRECTIONS:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and copy_grid[ni][nj] == 1:
                            uf.union(getIndex(i, j), getIndex(ni, nj))
        
        # Result array
        result = [0] * len(hits)
        
        # Reverse hits to simulate adding bricks back
        for k in range(len(hits) - 1, -1, -1):
            i, j = hits[k]
            if grid[i][j] == 0:
                continue
            
            # Number of stable bricks before adding this brick
            prev_size = uf.getSize(top)
            
            # Add the brick back
            copy_grid[i][j] = 1
            
            # Connect to the virtual top node if it's in the top row
            if i == 0:
                uf.union(getIndex(i, j), top)
            
            # Connect to adjacent bricks
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and copy_grid[ni][nj] == 1:
                    uf.union(getIndex(i, j), getIndex(ni, nj))
            
            # Number of stable bricks after adding this brick
            curr_size = uf.getSize(top)
            
            # The number of new bricks that became stable
            result[k] = max(0, curr_size - prev_size - 1)
        
        return result

def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    return Solution().hitBricks(grid, hits)