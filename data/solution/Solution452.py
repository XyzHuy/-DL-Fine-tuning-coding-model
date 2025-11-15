import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the balloons by their end coordinates
        points.sort(key=lambda x: x[1])
        
        # Initialize the number of arrows and the position of the last arrow shot
        arrows = 0
        last_arrow_position = -float('inf')
        
        for start, end in points:
            # If the current balloon starts after the last arrow shot, we need a new arrow
            if start > last_arrow_position:
                arrows += 1
                last_arrow_position = end
        
        return arrows

def findMinArrowShots(points: List[List[int]]) -> int:
    return Solution().findMinArrowShots(points)