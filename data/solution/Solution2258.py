import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions for moving in the grid (north, south, east, west)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize fire and person queues
        fire_q = deque()
        person_q = deque()
        
        # Initialize fire time grid
        fire_time = [[float('inf')] * n for _ in range(m)]
        
        # Populate the fire queue with all initial fire positions and set their time to 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_q.append((r, c))
                    fire_time[r][c] = 0
        
        # Perform BFS to calculate fire spread times
        while fire_q:
            r, c = fire_q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and fire_time[nr][nc] == float('inf'):
                    fire_time[nr][nc] = fire_time[r][c] + 1
                    fire_q.append((nr, nc))
        
        # Function to check if it's possible to reach the safehouse starting with a given delay
        def can_reach_safehouse(delay):
            person_time = [[float('inf')] * n for _ in range(m)]
            person_time[0][0] = delay
            person_q = deque([(0, 0)])
            
            while person_q:
                r, c = person_q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr == m - 1 and nc == n - 1:
                        if fire_time[nr][nc] < person_time[r][c] + 1:
                            return False
                        return person_time[r][c] + 1 <= fire_time[nr][nc]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and person_time[nr][nc] == float('inf'):
                        if person_time[r][c] + 1 < fire_time[nr][nc]:
                            person_time[nr][nc] = person_time[r][c] + 1
                            person_q.append((nr, nc))
            return False
        
        # Binary search for the maximum delay
        left, right = 0, 10**9
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach_safehouse(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result

def maximumMinutes(grid: List[List[int]]) -> int:
    return Solution().maximumMinutes(grid)