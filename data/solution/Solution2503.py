import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap to store the cells to visit, starting with the top-left cell
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        count = 0
        
        # Sort queries and keep track of their original indices
        sorted_queries = sorted((query, i) for i, query in enumerate(queries))
        result = [0] * len(queries)
        
        for query, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                _, x, y = heapq.heappop(min_heap)
                count += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
            result[original_index] = count
        
        return result

def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    return Solution().maxPoints(grid, queries)