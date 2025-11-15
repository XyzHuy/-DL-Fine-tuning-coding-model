import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        
        # Push all the boundary cells into the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        water_trapped = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    # Water can be trapped if the neighbor's height is less than the current boundary
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Push the neighbor into the heap with the higher boundary height
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return water_trapped

def trapRainWater(heightMap: List[List[int]]) -> int:
    return Solution().trapRainWater(heightMap)