import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_id = 2  # Start from 2 to avoid conflict with 0 and 1
        island_sizes = {}

        def dfs(x, y, island_id):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = island_id
            size = 1
            for dx, dy in directions:
                size += dfs(x + dx, y + dy, island_id)
            return size

        # Assign unique id to each island and calculate its size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size = dfs(i, j, island_id)
                    island_sizes[island_id] = island_size
                    island_id += 1

        max_island_size = max(island_sizes.values()) if island_sizes else 0

        # Check the effect of changing each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    connected_islands = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != 0:
                            connected_islands.add(grid[ni][nj])
                    new_island_size = 1 + sum(island_sizes[island] for island in connected_islands)
                    max_island_size = max(max_island_size, new_island_size)

        return max_island_size

def largestIsland(grid: List[List[int]]) -> int:
    return Solution().largestIsland(grid)