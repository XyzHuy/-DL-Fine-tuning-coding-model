import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import math

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Dictionary to store the lengths of diagonals and their respective endpoints
        diagonals = defaultdict(list)
        
        # Iterate over all pairs of points to find diagonals
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Calculate the length of the diagonal squared
                length_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
                
                # Calculate the midpoint of the diagonal
                mid = ((x1 + x2) / 2, (y1 + y2) / 2)
                
                # Store the points in the dictionary under the key (length_squared, mid)
                diagonals[(length_squared, mid)].append((i, j))
        
        min_area = float('inf')
        
        # Check all pairs of diagonals
        for diagonal, pairs in diagonals.items():
            for k in range(len(pairs)):
                for l in range(k + 1, len(pairs)):
                    # Get the indices of the points forming the diagonals
                    (i1, j1), (i2, j2) = pairs[k], pairs[l]
                    
                    # Get the coordinates of the points
                    x1, y1 = points[i1]
                    x2, y2 = points[j1]
                    x3, y3 = points[i2]
                    x4, y4 = points[j2]
                    
                    # Calculate the lengths of the sides using distance formula
                    side1 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    side2 = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
                    
                    # Calculate the area of the rectangle
                    area = side1 * side2
                    
                    # Update the minimum area found
                    min_area = min(min_area, area)
        
        # If no rectangle was found, return 0
        return min_area if min_area != float('inf') else 0

def minAreaFreeRect(points: List[List[int]]) -> float:
    return Solution().minAreaFreeRect(points)