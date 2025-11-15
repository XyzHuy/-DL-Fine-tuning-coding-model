import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        minHeap = [(0, 0, 0)]  # (time, row, col)
        
        while minHeap:
            time, x, y = heapq.heappop(minHeap)
            
            if visited[x][y]:
                continue
            
            visited[x][y] = True
            
            if x == m - 1 and y == n - 1:
                return time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if time + 1 >= grid[nx][ny]:
                        heapq.heappush(minHeap, (time + 1, nx, ny))
                    else:
                        # If we can't enter the cell directly, we wait until we can
                        wait_time = grid[nx][ny] - time
                        if wait_time % 2 == 0:
                            wait_time += 1  # Make it odd so we can wait and move back and forth
                        heapq.heappush(minHeap, (time + wait_time, nx, ny))
        
        return -1

def minimumTime(grid: List[List[int]]) -> int:
    return Solution().minimumTime(grid)