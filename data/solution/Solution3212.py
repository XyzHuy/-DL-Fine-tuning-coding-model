import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Iterate over all possible submatrices starting from (0,0)
        for i in range(m):
            for j in range(n):
                x_count = 0
                y_count = 0
                
                # Iterate over the submatrix starting from (0,0) to (i,j)
                for ii in range(i + 1):
                    for jj in range(j + 1):
                        if grid[ii][jj] == 'X':
                            x_count += 1
                        elif grid[ii][jj] == 'Y':
                            y_count += 1
                
                # Check if the submatrix is valid
                if x_count > 0 and x_count == y_count:
                    count += 1
        
        return count

def numberOfSubmatrices(grid: List[List[str]]) -> int:
    return Solution().numberOfSubmatrices(grid)