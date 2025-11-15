import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Initialize variables to track the bottom-left and top-right corners of the large rectangle
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        
        # Dictionary to count the occurrences of each corner
        corner_count = {}
        
        # Total area of all small rectangles
        total_area = 0
        
        # Iterate through each rectangle
        for x1, y1, x2, y2 in rectangles:
            # Update the coordinates of the large rectangle
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            
            # Calculate the area of the current rectangle
            total_area += (x2 - x1) * (y2 - y1)
            
            # Update the corner counts
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corner_count:
                    corner_count[corner] += 1
                else:
                    corner_count[corner] = 1
        
        # Check if the total area matches the area of the large rectangle
        if total_area != (max_x - min_x) * (max_y - min_y):
            return False
        
        # Check the corner points of the large rectangle
        large_corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        
        for corner in large_corners:
            if corner not in corner_count or corner_count[corner] != 1:
                return False
        
        # Check that all other corners appear an even number of times
        for corner, count in corner_count.items():
            if corner not in large_corners and count % 2 != 0:
                return False
        
        return True

def isRectangleCover(rectangles: List[List[int]]) -> bool:
    return Solution().isRectangleCover(rectangles)