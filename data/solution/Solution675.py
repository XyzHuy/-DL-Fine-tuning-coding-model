import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        m, n = len(forest), len(forest[0])
        
        # Step 1: Extract and sort trees by height
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        
        # Directions for moving in the grid: north, south, east, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Helper function to perform BFS and find the shortest path
        def bfs(start, end):
            queue = deque([start])
            visited = set([start])
            steps = 0
            
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if (x, y) == end:
                        return steps
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny] != 0:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                steps += 1
            return -1
        
        # Step 2: BFS from (0, 0) to the first tree, then to the next, and so on
        current_position = (0, 0)
        total_steps = 0
        
        for _, tx, ty in trees:
            steps = bfs(current_position, (tx, ty))
            if steps == -1:
                return -1
            total_steps += steps
            current_position = (tx, ty)
        
        return total_steps

def cutOffTree(forest: List[List[int]]) -> int:
    return Solution().cutOffTree(forest)