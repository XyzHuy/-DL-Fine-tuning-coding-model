import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            # Update the heights array
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == 1 else 0
            
            # Sort the heights array in descending order
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate the maximum area with the current configuration
            for i, height in enumerate(sorted_heights):
                max_area = max(max_area, height * (i + 1))
        
        return max_area

def largestSubmatrix(matrix: List[List[int]]) -> int:
    return Solution().largestSubmatrix(matrix)