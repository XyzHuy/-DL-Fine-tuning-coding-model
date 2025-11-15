import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])
        result = [[0] * n for _ in range(m)]
        
        # Convert mat1 to a list of lists of non-zero elements
        non_zero_mat1 = []
        for i in range(m):
            row = [(j, mat1[i][j]) for j in range(k) if mat1[i][j] != 0]
            non_zero_mat1.append(row)
        
        # Convert mat2 to a list of lists of non-zero elements (transpose for easier column access)
        non_zero_mat2 = []
        for j in range(n):
            col = [(i, mat2[i][j]) for i in range(k) if mat2[i][j] != 0]
            non_zero_mat2.append(col)
        
        # Perform the multiplication using the non-zero elements
        for i in range(m):
            for j in range(n):
                if non_zero_mat1[i] and non_zero_mat2[j]:
                    for col_index, val1 in non_zero_mat1[i]:
                        for row_index, val2 in non_zero_mat2[j]:
                            if col_index == row_index:
                                result[i][j] += val1 * val2
        
        return result

def multiply(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    return Solution().multiply(mat1, mat2)