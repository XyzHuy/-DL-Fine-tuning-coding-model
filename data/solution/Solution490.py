import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(maze), len(maze[0])
        visited = set()
        
        def dfs(x, y):
            if [x, y] == destination:
                return True
            if (x, y) in visited:
                return False
            visited.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x, y
                # Roll the ball until it hits a wall
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                # Recursively explore the new stopping point
                if dfs(nx, ny):
                    return True
            return False
        
        return dfs(start[0], start[1])

def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    return Solution().hasPath(maze, start, destination)