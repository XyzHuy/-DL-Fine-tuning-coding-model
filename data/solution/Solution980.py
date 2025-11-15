import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Directions for moving in the grid (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Find the start and end positions and count the number of empty squares
        start = end = None
        empty_squares = 1  # Start is considered as an empty square to walk over
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    empty_squares += 1
        
        # Depth-first search function
        def dfs(x, y, empty):
            # If we reach the end square, check if all empty squares have been visited
            if (x, y) == end:
                return empty == 0
            
            # Mark the current square as visited
            temp = grid[x][y]
            grid[x][y] = -1
            
            # Explore all 4 possible directions
            paths = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] >= 0:
                    paths += dfs(nx, ny, empty - 1)
            
            # Unmark the current square (backtrack)
            grid[x][y] = temp
            
            return paths
        
        # Start DFS from the start square
        return dfs(start[0], start[1], empty_squares)

def uniquePathsIII(grid: List[List[int]]) -> int:
    return Solution().uniquePathsIII(grid)