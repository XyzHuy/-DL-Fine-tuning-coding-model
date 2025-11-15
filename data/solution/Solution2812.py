import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Step 1: Calculate the shortest distance to the nearest thief for each cell
        distances = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        # Initialize the queue with all thief positions
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distances[r][c] = 0
                    queue.append((r, c))
        
        # BFS to fill the distances array
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == float('inf'):
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))
        
        # Step 2: Use a max-heap to find the path with the maximum safeness factor
        max_heap = [(-distances[0][0], 0, 0)]  # Store negative for max-heap behavior
        visited = set()
        visited.add((0, 0))
        
        while max_heap:
            current_safeness, r, c = heapq.heappop(max_heap)
            current_safeness = -current_safeness
            
            if r == n - 1 and c == n - 1:
                return current_safeness
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_safeness = min(current_safeness, distances[nr][nc])
                    heapq.heappush(max_heap, (-new_safeness, nr, nc))
                    visited.add((nr, nc))
        
        return 0

# Example usage:
# sol = Solution()
# print(sol.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))  # Output: 0
# print(sol.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))  # Output: 2
# print(sol.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))  # Output: 2

def maximumSafenessFactor(grid: List[List[int]]) -> int:
    return Solution().maximumSafenessFactor(grid)