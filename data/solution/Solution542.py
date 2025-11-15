import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # Initialize the distance matrix with -1
        dist = [[-1] * n for _ in range(m)]
        # Initialize the queue with all positions of 0s
        queue = deque()
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    dist[r][c] = 0
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        return dist

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    return Solution().updateMatrix(mat)