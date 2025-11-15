import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        # Initialize the number of ways to paint the first two posts
        same = k  # Last two posts have the same color
        diff = k * (k - 1)  # Last two posts have different colors
        total = same + diff
        
        for i in range(3, n + 1):
            new_same = diff  # If the last two posts are the same, the third one must be different from the second last
            new_diff = total * (k - 1)  # If the last two posts are different, the third one can be any color except the last one
            same = new_same
            diff = new_diff
            total = same + diff
        
        return total

def numWays(n: int, k: int) -> int:
    return Solution().numWays(n, k)