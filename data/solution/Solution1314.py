import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # Create a prefix sum matrix
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        
        # Create the result matrix
        result = [[0] * n for _ in range(m)]
        
        # Calculate the block sum for each cell
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
                r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
                result[i][j] = prefix_sum[r2][c2] - prefix_sum[r2][c1 - 1] - prefix_sum[r1 - 1][c2] + prefix_sum[r1 - 1][c1 - 1]
        
        return result

def matrixBlockSum(mat: List[List[int]], k: int) -> List[List[int]]:
    return Solution().matrixBlockSum(mat, k)