import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Check each element against the element diagonally above-left
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    return Solution().isToeplitzMatrix(matrix)