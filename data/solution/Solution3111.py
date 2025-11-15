import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        # Sort points by x-coordinate, and by y-coordinate if x-coordinates are the same
        points.sort()
        
        rectangles = 0
        i = 0
        n = len(points)
        
        while i < n:
            # Start a new rectangle at the current point's x-coordinate
            x1 = points[i][0]
            x2 = x1 + w
            
            # Move to the next point that is not covered by the current rectangle
            while i < n and points[i][0] <= x2:
                i += 1
            
            # Increment the rectangle count
            rectangles += 1
        
        return rectangles

def minRectanglesToCoverPoints(points: List[List[int]], w: int) -> int:
    return Solution().minRectanglesToCoverPoints(points, w)