import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Since the board is symmetric, we can reduce the problem to the first quadrant
        x, y = abs(x), abs(y)
        
        # Possible moves of a knight
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        # BFS initialization
        queue = [(0, 0, 0)]  # (current_x, current_y, steps)
        visited = set((0, 0))
        
        while queue:
            cx, cy, steps = queue.pop(0)
            
            # If we reach the target position
            if (cx, cy) == (x, y):
                return steps
            
            # Explore all possible moves
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                # We only need to consider positions that haven't been visited and are not too close to the origin
                if (nx, ny) not in visited and -2 < nx < x + 3 and -2 < ny < y + 3:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

def minKnightMoves(x: int, y: int) -> int:
    return Solution().minKnightMoves(x, y)