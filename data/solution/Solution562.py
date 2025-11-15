import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        m, n = len(mat), len(mat[0])
        max_length = 0
        
        # dp[i][j][0] - horizontal
        # dp[i][j][1] - vertical
        # dp[i][j][2] - diagonal
        # dp[i][j][3] - anti-diagonal
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Horizontal
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    # Vertical
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                    # Diagonal
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                    # Anti-diagonal
                    dp[i][j][3] = dp[i-1][j+1][3] + 1 if i > 0 and j < n - 1 else 1
                    
                    # Update the maximum length found
                    max_length = max(max_length, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        
        return max_length

def longestLine(mat: List[List[int]]) -> int:
    return Solution().longestLine(mat)