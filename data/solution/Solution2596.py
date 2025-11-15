import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        
        n = len(grid)
        # Possible knight moves
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        # Create a mapping from move number to position
        position = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                position[grid[i][j]] = (i, j)
        
        # Check if each move is valid
        for step in range(1, n * n):
            prev_x, prev_y = position[step - 1]
            curr_x, curr_y = position[step]
            
            # Check if the difference between positions is a valid knight move
            if (abs(prev_x - curr_x), abs(prev_y - curr_y)) not in [(2, 1), (1, 2)]:
                return False
        
        return True

def checkValidGrid(grid: List[List[int]]) -> bool:
    return Solution().checkValidGrid(grid)