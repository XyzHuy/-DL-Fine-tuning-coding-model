import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap to store (effort, row, col)
        min_heap = [(0, 0, 0)]
        # Set to keep track of visited cells
        visited = set()
        # Dictionary to store the minimum effort to reach each cell
        dist = {(0, 0): 0}
        
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            
            # If we reach the bottom-right cell, return the effort
            if x == rows - 1 and y == cols - 1:
                return effort
            
            # If the cell is already visited, skip it
            if (x, y) in visited:
                continue
            
            # Mark the cell as visited
            visited.add((x, y))
            
            # Explore all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new cell is within bounds
                if 0 <= nx < rows and 0 <= ny < cols:
                    # Calculate the effort to move to the new cell
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    # If the new effort is less than the previously recorded effort for this cell
                    if (nx, ny) not in dist or new_effort < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_effort
                        heapq.heappush(min_heap, (new_effort, nx, ny))
        
        return -1  # This line should never be reached if the input is valid

def minimumEffortPath(heights: List[List[int]]) -> int:
    return Solution().minimumEffortPath(heights)