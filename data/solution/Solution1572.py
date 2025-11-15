import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_diagonal_sum = 0
        secondary_diagonal_sum = 0
        
        for i in range(n):
            primary_diagonal_sum += mat[i][i]
            secondary_diagonal_sum += mat[i][n - 1 - i]
        
        # If the matrix has an odd dimension, subtract the middle element once as it's counted twice
        if n % 2 == 1:
            middle_element = mat[n // 2][n // 2]
            return primary_diagonal_sum + secondary_diagonal_sum - middle_element
        
        return primary_diagonal_sum + secondary_diagonal_sum

def diagonalSum(mat: List[List[int]]) -> int:
    return Solution().diagonalSum(mat)