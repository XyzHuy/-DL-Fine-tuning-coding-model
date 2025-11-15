import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxA(self, n: int) -> int:
        # If n is less than or equal to 3, the maximum number of 'A's is n itself
        if n <= 3:
            return n
        
        # Create a list to store the maximum number of 'A's we can get with i key presses
        dp = [i for i in range(n + 1)]
        
        # Starting from 4 because with 3 or less key presses, the best we can do is press 'A' that many times
        for i in range(4, n + 1):
            # We try to find the best combination of Ctrl-A, Ctrl-C, and multiple Ctrl-Vs
            # j is the number of key presses we use to get the initial sequence to copy
            for j in range(i - 1):
                # We need at least 3 more key presses for Ctrl-A, Ctrl-C, and the first Ctrl-V
                if i - j - 1 < 2:
                    continue
                # dp[j] is the number of 'A's we get from j key presses
                # (i - j - 1) is the number of Ctrl-V operations we can perform after copying
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        
        return dp[n]

def maxA(n: int) -> int:
    return Solution().maxA(n)