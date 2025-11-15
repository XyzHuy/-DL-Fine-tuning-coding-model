import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        
        # Use a set to store unique points
        point_set = set(tuple(point) for point in points)
        
        # Find the minimum and maximum x-coordinates
        min_x = min(point[0] for point in points)
        max_x = max(point[0] for point in points)
        
        # Calculate the potential reflection line x-coordinate
        reflection_line = min_x + max_x
        
        # Check for each point if its reflected counterpart exists
        for x, y in point_set:
            reflected_x = reflection_line - x
            if (reflected_x, y) not in point_set:
                return False
        
        return True

def isReflected(points: List[List[int]]) -> bool:
    return Solution().isReflected(points)