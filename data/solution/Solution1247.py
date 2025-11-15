import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Count the mismatches
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1
        
        # If the total number of mismatches is odd, it's impossible to make the strings equal
        if (xy + yx) % 2 != 0:
            return -1
        
        # Calculate the minimum number of swaps
        swaps = xy // 2 + yx // 2
        # If there is one 'xy' and one 'yx' mismatch left, we need two swaps
        if xy % 2 != 0:
            swaps += 2
        
        return swaps

def minimumSwap(s1: str, s2: str) -> int:
    return Solution().minimumSwap(s1, s2)