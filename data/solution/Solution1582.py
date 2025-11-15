import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Count the number of 1s in each row and each column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # Find special positions
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_counts[i] == 1 and col_counts[j] == 1:
                    special_count += 1
        
        return special_count

def numSpecial(mat: List[List[int]]) -> int:
    return Solution().numSpecial(mat)