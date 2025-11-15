import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # dp[r1][c1][c2] will store the maximum number of cherries collected when one agent is at (r1, c1) and the other is at (r2, c2)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]
        
        for t in range(1, 2 * n - 1):
            for r1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                c1 = t - r1
                if grid[r1][c1] == -1:
                    continue
                for r2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    c2 = t - r2
                    if grid[r2][c2] == -1:
                        continue
                    # Calculate the cherries collected at current positions
                    cherries_here = grid[r1][c1] if (r1, c1) == (r2, c2) else grid[r1][c1] + grid[r2][c2]
                    # Check all possible previous positions
                    for dr1 in range(2):
                        for dr2 in range(2):
                            r1_prev, c1_prev = r1 - dr1, c1 - (1 - dr1)
                            r2_prev, c2_prev = r2 - dr2, c2 - (1 - dr2)
                            if r1_prev >= 0 and c1_prev >= 0 and r2_prev >= 0 and c2_prev >= 0 and dp[r1_prev][c1_prev][r2_prev] != -1:
                                dp[r1][c1][r2] = max(dp[r1][c1][r2], dp[r1_prev][c1_prev][r2_prev] + cherries_here)
        
        return max(0, dp[n - 1][n - 1][n - 1])

# Example usage:
# sol = Solution()
# grid1 = [[0,1,-1],[1,0,-1],[1,1,1]]
# print(sol.cherryPickup(grid1))  # Output: 5

# grid2 = [[1,1,-1],[1,-1,1],[-1,1,1]]
# print(sol.cherryPickup(grid2))  # Output: 0

def cherryPickup(grid: List[List[int]]) -> int:
    return Solution().cherryPickup(grid)