import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0  # Mark the cell as visited
            # Check all four directions and ensure all parts of the island in grid2 are also land in grid1
            return (grid1[i][j] == 1) & dfs(i + 1, j) & dfs(i - 1, j) & dfs(i, j + 1) & dfs(i, j - 1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1
        return count

def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    return Solution().countSubIslands(grid1, grid2)