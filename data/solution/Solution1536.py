import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Calculate the number of trailing zeros for each row
        trailing_zeros = [0] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    trailing_zeros[i] += 1
                else:
                    break
        
        swaps = 0
        for i in range(n):
            # We need at least (n - i - 1) trailing zeros in the i-th row
            if trailing_zeros[i] < n - i - 1:
                # Find a row below the i-th row with enough trailing zeros
                found = False
                for j in range(i + 1, n):
                    if trailing_zeros[j] >= n - i - 1:
                        # Swap rows i and j
                        for k in range(j, i, -1):
                            trailing_zeros[k], trailing_zeros[k - 1] = trailing_zeros[k - 1], trailing_zeros[k]
                            swaps += 1
                        found = True
                        break
                if not found:
                    return -1
        return swaps

def minSwaps(grid: List[List[int]]) -> int:
    return Solution().minSwaps(grid)