import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, direction):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0  # Mark the cell as visited
                path.append(direction)
                dfs(i + 1, j, 'd')  # down
                dfs(i - 1, j, 'u')  # up
                dfs(i, j + 1, 'r')  # right
                dfs(i, j - 1, 'l')  # left
                path.append('b')  # backtracking
            return path
        
        shapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, 'o')  # origin
                    shapes.add(tuple(path))
        
        return len(shapes)

def numDistinctIslands(grid: List[List[int]]) -> int:
    return Solution().numDistinctIslands(grid)