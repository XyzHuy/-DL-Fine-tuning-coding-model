import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def is_inside_circle(x, y, cx, cy, r):
            return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2
        
        # Define the grid based on the constraints
        max_x = max(circle[0] + circle[2] for circle in circles)
        max_y = max(circle[1] + circle[2] for circle in circles)
        
        # Set to store unique lattice points
        lattice_points = set()
        
        # Check each point in the grid
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                for cx, cy, r in circles:
                    if is_inside_circle(x, y, cx, cy, r):
                        lattice_points.add((x, y))
                        break
        
        return len(lattice_points)

def countLatticePoints(circles: List[List[int]]) -> int:
    return Solution().countLatticePoints(circles)