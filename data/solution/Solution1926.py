import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Get the dimensions of the maze
        m, n = len(maze), len(maze[0])
        
        # Initialize the queue for BFS with the entrance position and step count
        queue = deque([(entrance[0], entrance[1], 0)])
        
        # Mark the entrance as visited by setting it to '+'
        maze[entrance[0]][entrance[1]] = '+'
        
        # Perform BFS
        while queue:
            x, y, steps = queue.popleft()
            
            # Check all four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds and not a wall
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    # Mark the cell as visited
                    maze[nx][ny] = '+'
                    
                    # Check if the new position is an exit
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return steps + 1
                    
                    # Add the new position to the queue with incremented step count
                    queue.append((nx, ny, steps + 1))
        
        # If no exit is found, return -1
        return -1

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    return Solution().nearestExit(maze, entrance)