import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize a 3D DP array with dimensions (maxMove+1) x m x n
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        
        # Directions for moving the ball: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Iterate over the number of moves
        for moves in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            # If the ball goes out of bounds, count this path
                            dp[moves][i][j] = (dp[moves][i][j] + 1) % MOD
                        else:
                            # Otherwise, add the number of ways to reach (ni, nj) in (moves-1) moves
                            dp[moves][i][j] = (dp[moves][i][j] + dp[moves - 1][ni][nj]) % MOD
        
        return dp[maxMove][startRow][startColumn]

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    return Solution().findPaths(m, n, maxMove, startRow, startColumn)