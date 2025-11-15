import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # Place the minimum of rowSum[i] and colSum[j] in matrix[i][j]
                matrix[i][j] = min(rowSum[i], colSum[j])
                # Decrease the placed value from the respective rowSum and colSum
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        
        return matrix

def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    return Solution().restoreMatrix(rowSum, colSum)