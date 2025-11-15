import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Initialize lists to store the count of ones and zeros in each row and column
        onesRow = [0] * m
        zerosRow = [0] * m
        onesCol = [0] * n
        zerosCol = [0] * n
        
        # Calculate the number of ones and zeros in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        
        # Create the difference matrix
        diff = [[0] * n for _ in range(m)]
        
        # Fill the difference matrix using the formula
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return diff

def onesMinusZeros(grid: List[List[int]]) -> List[List[int]]:
    return Solution().onesMinusZeros(grid)