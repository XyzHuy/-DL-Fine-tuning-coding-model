import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        
        # Calculate the slope between the first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Avoid division by zero by using cross multiplication
        dx = x1 - x0
        dy = y1 - y0
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Check if the cross product of the vectors (x1-x0, y1-y0) and (x-x0, y-y0) is zero
            if dy * (x - x0) != dx * (y - y0):
                return False
        
        return True

def checkStraightLine(coordinates: List[List[int]]) -> bool:
    return Solution().checkStraightLine(coordinates)