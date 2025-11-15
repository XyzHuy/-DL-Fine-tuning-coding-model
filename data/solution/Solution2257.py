import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[0] * n for _ in range(m)]
        
        # Place walls on the grid
        for r, c in walls:
            grid[r][c] = 'W'
        
        # Place guards on the grid
        for r, c in guards:
            grid[r][c] = 'G'
        
        # Directions for north, east, south, west
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Function to mark guarded cells
        def mark_guarded(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 'W' or grid[nr][nc] == 'G':
                        break
                    grid[nr][nc] = 'X'
                    nr += dr
                    nc += dc
        
        # Mark cells guarded by each guard
        for r, c in guards:
            mark_guarded(r, c)
        
        # Count unguarded cells
        unguarded_count = sum(grid[r][c] == 0 for r in range(m) for c in range(n))
        
        return unguarded_count

def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    return Solution().countUnguarded(m, n, guards, walls)