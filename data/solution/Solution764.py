import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Create a set of mines for O(1) look-up time
        mines_set = set(tuple(mine) for mine in mines)
        
        # Initialize the dp array
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
        
        # Fill the dp array for left and top directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    top = dp[i-1][j][0] if i > 0 else 0
                    left = dp[i][j-1][3] if j > 0 else 0
                    dp[i][j][0] = top + 1
                    dp[i][j][3] = left + 1
        
        # Fill the dp array for right and bottom directions and calculate the result
        order = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    bottom = dp[i+1][j][2] if i < n-1 else 0
                    right = dp[i][j+1][1] if j < n-1 else 0
                    dp[i][j][2] = bottom + 1
                    dp[i][j][1] = right + 1
                    # The order of the plus sign is the minimum of the four directions
                    order = max(order, min(dp[i][j]))
        
        return order

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    return Solution().orderOfLargestPlusSign(n, mines)