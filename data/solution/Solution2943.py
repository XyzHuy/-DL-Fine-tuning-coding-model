import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # Sort the bars
        hBars.sort()
        vBars.sort()
        
        # Function to find the maximum number of consecutive bars that can be removed
        def max_consecutive_bars(bars):
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_consecutive += 1
                else:
                    max_consecutive = max(max_consecutive, current_consecutive)
                    current_consecutive = 1
            
            max_consecutive = max(max_consecutive, current_consecutive)
            return max_consecutive
        
        # Find the maximum number of consecutive horizontal and vertical bars that can be removed
        max_h_consecutive = max_consecutive_bars(hBars)
        max_v_consecutive = max_consecutive_bars(vBars)
        
        # The side length of the largest square hole
        side_length = min(max_h_consecutive + 1, max_v_consecutive + 1)
        
        # The area of the largest square hole
        return side_length * side_length

def maximizeSquareHoleArea(n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
    return Solution().maximizeSquareHoleArea(n, m, hBars, vBars)