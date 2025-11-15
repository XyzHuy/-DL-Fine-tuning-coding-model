import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Ensure the first column has all 1s by toggling rows if necessary
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        
        # Toggle columns if the number of 0s is greater than the number of 1s
        cols = len(grid[0])
        rows = len(grid)
        for col in range(1, cols):
            count_ones = sum(grid[row][col] for row in range(rows))
            if count_ones < rows - count_ones:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]
        
        # Calculate the score of the matrix
        score = 0
        for row in grid:
            binary_number = int(''.join(map(str, row)), 2)
            score += binary_number
        
        return score

def matrixScore(grid: List[List[int]]) -> int:
    return Solution().matrixScore(grid)