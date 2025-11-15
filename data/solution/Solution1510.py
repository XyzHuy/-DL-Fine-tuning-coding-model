import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Initialize a dp array of size n+1 with False
        dp = [False] * (n + 1)
        
        # Iterate over each number of stones from 1 to n
        for i in range(1, n + 1):
            # Check all possible square numbers that can be removed
            j = 1
            while j * j <= i:
                # If removing j*j stones leaves the opponent in a losing position, set dp[i] to True
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        
        # Return the result for n stones
        return dp[n]

def winnerSquareGame(n: int) -> bool:
    return Solution().winnerSquareGame(n)