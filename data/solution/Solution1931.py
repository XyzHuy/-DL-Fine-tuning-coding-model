import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Generate all valid columns
        def generate_valid_columns():
            valid_columns = []
            
            def backtrack(column, index):
                if index == m:
                    valid_columns.append(tuple(column))
                    return
                for color in range(3):
                    if index == 0 or column[index - 1] != color:
                        column[index] = color
                        backtrack(column, index + 1)
            
            backtrack([0] * m, 0)
            return valid_columns
        
        valid_columns = generate_valid_columns()
        
        # Step 2: Check if two columns can be adjacent
        def are_compatible(col1, col2):
            return all(c1 != c2 for c1, c2 in zip(col1, col2))
        
        # Step 3: Initialize dp table
        dp = {mask: 1 for mask in valid_columns}
        
        # Step 4: Fill dp table
        for _ in range(1, n):
            next_dp = {mask: 0 for mask in valid_columns}
            for col1 in valid_columns:
                for col2 in valid_columns:
                    if are_compatible(col1, col2):
                        next_dp[col2] = (next_dp[col2] + dp[col1]) % MOD
            dp = next_dp
        
        # Step 5: Sum up the results for the last column
        return sum(dp.values()) % MOD

def colorTheGrid(m: int, n: int) -> int:
    return Solution().colorTheGrid(m, n)