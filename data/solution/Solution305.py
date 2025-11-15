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
        self.count = 0

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        # Union by rank
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        self.count -= 1
        return True

    def getCount(self):
        return self.count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        result = []
        island_count = 0

        for r, c in positions:
            if grid[r][c] == 1:
                result.append(island_count)
                continue

            grid[r][c] = 1
            island_count += 1
            index = r * n + c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    neighbor_index = nr * n + nc
                    if uf.union(index, neighbor_index):
                        island_count -= 1

            result.append(island_count)

        return result

def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    return Solution().numIslands2(m, n, positions)