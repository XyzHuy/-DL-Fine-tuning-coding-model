import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def is_border(r, c):
            # Check if the current cell is on the border of the grid
            if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
                return True
            # Check if the current cell is adjacent to a cell with a different color
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if grid[nr][nc] != original_color:
                    return True
            return False

        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if (r, c) in visited:
                return
            if grid[r][c] != original_color:
                return
            
            visited.add((r, c))
            
            if is_border(r, c):
                border_cells.append((r, c))
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)

        original_color = grid[row][col]
        visited = set()
        border_cells = []
        
        dfs(row, col)
        
        for r, c in border_cells:
            grid[r][c] = color
        
        return grid

def colorBorder(grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    return Solution().colorBorder(grid, row, col, color)