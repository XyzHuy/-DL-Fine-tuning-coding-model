import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # List to store positions of cells with excess stones
        excess = []
        # List to store positions of cells that need stones
        need = []
        
        # Populate the excess and need lists
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    need.append((i, j))
                elif grid[i][j] > 1:
                    excess.append((i, j, grid[i][j] - 1))
        
        # Helper function to calculate Manhattan distance between two cells
        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        # Recursive function to try placing stones in need cells
        def dfs(index):
            if index == len(need):
                return 0
            min_moves = float('inf')
            for i in range(len(excess)):
                if excess[i][2] > 0:
                    x1, y1, _ = excess[i]
                    x2, y2 = need[index]
                    # Calculate the distance and move the stone
                    moves = distance(x1, y1, x2, y2)
                    excess[i] = (x1, y1, excess[i][2] - 1)
                    # Recur for the next need cell
                    min_moves = min(min_moves, moves + dfs(index + 1))
                    # Backtrack
                    excess[i] = (x1, y1, excess[i][2] + 1)
            return min_moves
        
        return dfs(0)

# Example usage:
# sol = Solution()
# print(sol.minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))  # Output: 3
# print(sol.minimumMoves([[1,3,0],[1,0,0],[1,0,3]]))  # Output: 4

def minimumMoves(grid: List[List[int]]) -> int:
    return Solution().minimumMoves(grid)