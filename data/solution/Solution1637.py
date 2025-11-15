import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract the x-coordinates from the points
        x_coords = [point[0] for point in points]
        
        # Sort the x-coordinates
        x_coords.sort()
        
        # Calculate the maximum width of the vertical area
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])
        
        return max_width

def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
    return Solution().maxWidthOfVerticalArea(points)