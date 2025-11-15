import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def flips_to_palindrome(row_or_col):
            flips = 0
            for i in range(len(row_or_col) // 2):
                if row_or_col[i] != row_or_col[-i-1]:
                    flips += 1
            return flips
        
        # Calculate the number of flips needed to make each row palindromic
        row_flips = [flips_to_palindrome(grid[i]) for i in range(m)]
        # Calculate the number of flips needed to make each column palindromic
        col_flips = [flips_to_palindrome([grid[j][i] for j in range(m)]) for i in range(n)]
        
        # Total flips to make all rows palindromic
        min_row_flips = sum(row_flips)
        # Total flips to make all columns palindromic
        min_col_flips = sum(col_flips)
        
        # Choose the minimum of the two
        return min(min_row_flips, min_col_flips)

def minFlips(grid: List[List[int]]) -> int:
    return Solution().minFlips(grid)