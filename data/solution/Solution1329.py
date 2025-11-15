import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Dictionary to hold the diagonals
        diagonals = defaultdict(list)
        
        # Collect all elements of the same diagonal
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i - j].append(mat[i][j])
        
        # Sort each diagonal
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        
        # Place the sorted elements back into the matrix
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat

def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    return Solution().diagonalSort(mat)