import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        m, n = len(mat), len(mat[0])
        # Create a helper array to store the number of consecutive 1s ending at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Fill the dp array
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
        
        count = 0
        
        # For each cell, use it as the bottom-right corner of the rectangle and count all possible rectangles
        for i in range(m):
            for j in range(n):
                min_width = float('inf')
                for k in range(i, -1, -1):
                    if dp[k][j] == 0:
                        break
                    min_width = min(min_width, dp[k][j])
                    count += min_width
        
        return count

def numSubmat(mat: List[List[int]]) -> int:
    return Solution().numSubmat(mat)