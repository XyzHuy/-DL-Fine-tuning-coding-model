import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        n, m = len(land), len(land[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize queues for flood and person BFS
        flood_q = deque()
        person_q = deque()
        
        # Find the start and flood positions
        for i in range(n):
            for j in range(m):
                if land[i][j] == 'S':
                    person_q.append((i, j))
                elif land[i][j] == '*':
                    flood_q.append((i, j))
        
        # Mark the start position as visited
        land[person_q[0][0]][person_q[0][1]] = 'V'
        
        time = 0
        
        # Perform BFS for both flood and person
        while person_q:
            # First, expand the flood for this time step
            for _ in range(len(flood_q)):
                x, y = flood_q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == '.':
                        land[nx][ny] = '*'
                        flood_q.append((nx, ny))
            
            # Then, move the person for this time step
            for _ in range(len(person_q)):
                x, y = person_q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if land[nx][ny] == 'D':
                            return time + 1  # Reached the destination
                        elif land[nx][ny] == '.':
                            land[nx][ny] = 'V'  # Mark as visited
                            person_q.append((nx, ny))
            
            time += 1
        
        return -1  # Impossible to reach the destination

def minimumSeconds(land: List[List[str]]) -> int:
    return Solution().minimumSeconds(land)