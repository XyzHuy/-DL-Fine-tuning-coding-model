import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Add the edges to the cuts
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        
        # Find the maximum distance between consecutive horizontal cuts
        max_h = max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts)))
        
        # Find the maximum distance between consecutive vertical cuts
        max_v = max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts)))
        
        # The maximum area is the product of these two maximum distances
        return (max_h * max_v) % (10**9 + 7)

def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    return Solution().maxArea(h, w, horizontalCuts, verticalCuts)