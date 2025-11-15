import random
import functools
import collections
import string
import math
import datetime


from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = set()
        
        # Directions for moving in the grid (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x: int, y: int, island: List[Tuple[int, int]]) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return
            grid[x][y] = 0  # Mark the cell as visited
            island.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy, island)
        
        def normalize(island: List[Tuple[int, int]]) -> Tuple[Tuple[int, int]]:
            # Get all possible rotations and reflections
            shapes = []
            for _ in range(4):
                # Rotate 90 degrees
                island = [(y, -x) for x, y in island]
                shapes.append(sorted(island))
                # Reflect horizontally
                shapes.append(sorted([(-x, y) for x, y in island]))
            # Reflect vertically
            shapes.append(sorted([(x, -y) for x, y in island]))
            shapes.append(sorted([(-x, -y) for x, y in island]))
            
            # Normalize by subtracting the minimum x and y coordinates
            min_x = min(p[0] for p in shapes[0])
            min_y = min(p[1] for p in shapes[0])
            normalized = tuple(sorted((x - min_x, y - min_y) for x, y in shapes[0]))
            
            # Find the lexicographically smallest shape among all transformations
            for shape in shapes[1:]:
                min_x = min(p[0] for p in shape)
                min_y = min(p[1] for p in shape)
                norm_shape = tuple(sorted((x - min_x, y - min_y) for x, y in shape))
                if norm_shape < normalized:
                    normalized = norm_shape
            
            return normalized
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    # Normalize the island shape and add to the set
                    islands.add(normalize(island))
        
        return len(islands)

def numDistinctIslands2(grid: List[List[int]]) -> int:
    return Solution().numDistinctIslands2(grid)