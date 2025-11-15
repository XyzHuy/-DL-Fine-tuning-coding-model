import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list to store the minimum number of perfect squares for each number up to n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be represented by 0 perfect squares
        
        # Precompute all perfect squares less than or equal to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # Fill the dp array
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

def numSquares(n: int) -> int:
    return Solution().numSquares(n)