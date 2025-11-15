import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort the cuts to process the largest cuts first
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        ans = i = j = 0
        h = v = 1  # Initialize the height and width of the current piece of cake
        
        while i < len(horizontalCut) or j < len(verticalCut):
            if j == len(verticalCut) or (i < len(horizontalCut) and horizontalCut[i] > verticalCut[j]):
                # Perform a horizontal cut
                ans += horizontalCut[i] * v
                h += 1
                i += 1
            else:
                # Perform a vertical cut
                ans += verticalCut[j] * h
                v += 1
                j += 1
        
        # Add the cost of the final cuts to reach 1x1 pieces
        ans += h * (n - j - 1)
        ans += v * (m - i - 1)
        
        return ans

def minimumCost(m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    return Solution().minimumCost(m, n, horizontalCut, verticalCut)