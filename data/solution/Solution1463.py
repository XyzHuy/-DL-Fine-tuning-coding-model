import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(row, col1, col2):
            # Base case: if robots go out of bounds
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0
            
            # Current cherries collected by both robots
            cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            
            # If we are at the last row, return the cherries collected
            if row == rows - 1:
                return cherries
            
            # Explore all possible moves for both robots
            max_cherries = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(row + 1, col1 + dc1, col2 + dc2))
            
            # Return the total cherries collected from this state
            return cherries + max_cherries
        
        # Start the dp from the top row with both robots at the edges
        return dp(0, 0, cols - 1)

def cherryPickup(grid: List[List[int]]) -> int:
    return Solution().cherryPickup(grid)