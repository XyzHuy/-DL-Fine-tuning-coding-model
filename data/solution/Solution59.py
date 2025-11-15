import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the initial boundaries of the spiral
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # Start filling the matrix with numbers from 1 to n^2
        num = 1
        while top <= bottom and left <= right:
            # Fill the top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # Fill the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Fill the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
            # Fill the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        
        return matrix

def generateMatrix(n: int) -> List[List[int]]:
    return Solution().generateMatrix(n)