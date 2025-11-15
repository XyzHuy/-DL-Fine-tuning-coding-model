import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = {}
        
        def dp(l, r, k):
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            if l > r:
                return 0
            
            # Extend the segment of the same color as boxes[l]
            while r > l and boxes[r] == boxes[l]:
                r -= 1
                k += 1
            
            # Points for removing the current segment
            points = (k + 1) * (k + 1) + dp(l + 1, r, 0)
            
            # Try to merge non-contiguous segments of the same color
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    points = max(points, dp(l + 1, i - 1, 0) + dp(i, r, k + 1))
            
            memo[(l, r, k)] = points
            return points
        
        return dp(0, len(boxes) - 1, 0)

def removeBoxes(boxes: List[int]) -> int:
    return Solution().removeBoxes(boxes)