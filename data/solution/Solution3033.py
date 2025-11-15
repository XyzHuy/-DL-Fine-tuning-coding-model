import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Find the maximum value in each column
        num_cols = len(matrix[0])
        max_in_columns = [max(matrix[row][col] for row in range(len(matrix))) for col in range(num_cols)]
        
        # Replace -1 in each column with the maximum value of that column
        for row in range(len(matrix)):
            for col in range(num_cols):
                if matrix[row][col] == -1:
                    matrix[row][col] = max_in_columns[col]
        
        return matrix

def modifiedMatrix(matrix: List[List[int]]) -> List[List[int]]:
    return Solution().modifiedMatrix(matrix)