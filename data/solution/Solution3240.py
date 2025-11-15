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
        ans = 0
        
        # Check and flip the outer layers of the grid to make them palindromic
        for i in range(m // 2):
            for j in range(n // 2):
                x, y = m - i - 1, n - j - 1
                cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y]
                ans += min(cnt1, 4 - cnt1)
        
        # If both dimensions are odd, handle the center cell separately
        if m % 2 and n % 2:
            ans += grid[m // 2][n // 2]
        
        # Calculate the number of 1's in the middle row (if m is odd)
        cnt1 = 0
        diff = 0
        if m % 2:
            for j in range(n // 2):
                if grid[m // 2][j] == grid[m // 2][n - j - 1]:
                    cnt1 += grid[m // 2][j] * 2
                else:
                    diff += 1
        
        # Calculate the number of 1's in the middle column (if n is odd)
        if n % 2:
            for i in range(m // 2):
                if grid[i][n // 2] == grid[m - i - 1][n // 2]:
                    cnt1 += grid[i][n // 2] * 2
                else:
                    diff += 1
        
        # Adjust the answer to ensure the total number of 1's is divisible by 4
        ans += diff if cnt1 % 4 == 0 or diff else 2
        
        return ans

def minFlips(grid: List[List[int]]) -> int:
    return Solution().minFlips(grid)