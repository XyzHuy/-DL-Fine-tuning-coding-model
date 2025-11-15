import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        horizontal = [[0] * cols for _ in range(rows)]
        vertical = [[0] * cols for _ in range(rows)]
        
        # Fill the horizontal and vertical arrays
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    horizontal[i][j] = horizontal[i][j-1] + 1 if j > 0 else 1
                    vertical[i][j] = vertical[i-1][j] + 1 if i > 0 else 1
        
        # Find the largest square with 1s on its border
        max_side = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if grid[i][j] == 0:
                    continue
                side = min(horizontal[i][j], vertical[i][j])
                while side > max_side:
                    if horizontal[i-side+1][j] >= side and vertical[i][j-side+1] >= side:
                        max_side = side
                    side -= 1
        
        return max_side * max_side

# Example usage:
# sol = Solution()
# print(sol.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))  # Output: 9
# print(sol.largest1BorderedSquare([[1,1,0,0]]))  # Output: 1

def largest1BorderedSquare(grid: List[List[int]]) -> int:
    return Solution().largest1BorderedSquare(grid)