import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Initialize the dp array
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        m = 0
        
        # Iterate until we find the minimum number of moves
        while dp[m][k] < n:
            m += 1
            for i in range(1, k + 1):
                dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1
        
        return m

def superEggDrop(k: int, n: int) -> int:
    return Solution().superEggDrop(k, n)