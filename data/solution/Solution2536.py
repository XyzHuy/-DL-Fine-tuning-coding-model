import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Initialize the difference matrix with zeros
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Apply the difference updates for each query
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Initialize the result matrix with zeros
        result = [[0] * n for _ in range(n)]
        
        # Compute the prefix sum to get the final matrix values
        for i in range(n):
            for j in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
                result[i][j] = diff[i][j]
        
        return result

def rangeAddQueries(n: int, queries: List[List[int]]) -> List[List[int]]:
    return Solution().rangeAddQueries(n, queries)