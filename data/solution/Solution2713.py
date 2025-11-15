import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Create a list of cells with their values
        cells = [(mat[i][j], i, j) for i in range(m) for j in range(n)]
        
        # Step 2: Sort the cells by their values
        cells.sort()
        
        # Step 3: Initialize dp table
        dp = [[0] * n for _ in range(m)]
        
        # Step 4: Dictionaries to store the maximum values for each row and column
        row_max = defaultdict(int)
        col_max = defaultdict(int)
        
        # Step 5: Process each cell in the sorted order
        max_cells = 0
        i = 0
        while i < len(cells):
            # Process all cells with the same value together
            value = cells[i][0]
            temp_row_max = row_max.copy()
            temp_col_max = col_max.copy()
            
            while i < len(cells) and cells[i][0] == value:
                _, r, c = cells[i]
                # Step 6: Update dp[r][c] with the maximum value from row_max and col_max
                dp[r][c] = max(row_max[r], col_max[c]) + 1
                # Step 7: Update the temporary row_max and col_max
                temp_row_max[r] = max(temp_row_max[r], dp[r][c])
                temp_col_max[c] = max(temp_col_max[c], dp[r][c])
                i += 1
            
            # Step 8: Update the global row_max and col_max after processing all cells with the same value
            for r, val in temp_row_max.items():
                row_max[r] = val
            for c, val in temp_col_max.items():
                col_max[c] = val
        
        # Step 9: Find the maximum value in the dp table
        for i in range(m):
            for j in range(n):
                max_cells = max(max_cells, dp[i][j])
        
        return max_cells

def maxIncreasingCells(mat: List[List[int]]) -> int:
    return Solution().maxIncreasingCells(mat)