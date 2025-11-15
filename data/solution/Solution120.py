import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # Initialize a DP array with an extra column for easier calculations
        dp = [0] * (n + 1)
        
        # Start from the bottom of the triangle and move upwards
        for row in range(n - 1, -1, -1):
            for col in range(row + 1):
                # Update the DP array with the minimum path sum for each element
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]
        
        # The top element now contains the minimum path sum
        return dp[0]

def minimumTotal(triangle: List[List[int]]) -> int:
    return Solution().minimumTotal(triangle)