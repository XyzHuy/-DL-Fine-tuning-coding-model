import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [-1] * n
        
        for ball in range(n):
            col = ball
            for row in range(m):
                next_col = col + grid[row][col]
                if next_col < 0 or next_col >= n or grid[row][col] != grid[row][next_col]:
                    break
                col = next_col
            else:
                result[ball] = col
        
        return result

def findBall(grid: List[List[int]]) -> List[int]:
    return Solution().findBall(grid)