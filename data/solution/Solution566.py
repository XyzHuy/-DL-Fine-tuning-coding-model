import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Get the dimensions of the original matrix
        m, n = len(mat), len(mat[0])
        
        # Check if the reshape operation is possible
        if m * n != r * c:
            return mat
        
        # Flatten the original matrix
        flat = [mat[i][j] for i in range(m) for j in range(n)]
        
        # Reshape the flattened list into the desired matrix
        reshaped = [flat[i * c:(i + 1) * c] for i in range(r)]
        
        return reshaped

def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    return Solution().matrixReshape(mat, r, c)