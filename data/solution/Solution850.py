import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Extract all unique y-coordinates
        y_coords = set()
        for x1, y1, x2, y2 in rectangles:
            y_coords.add(y1)
            y_coords.add(y2)
        
        # Sort the y-coordinates
        y_coords = sorted(y_coords)
        
        # Create a mapping from y-coordinate to its index
        y_index = {y: i for i, y in enumerate(y_coords)}
        
        # Sweep line algorithm
        events = []
        for x1, y1, x2, y2 in rectangles:
            # 0 for start of rectangle, 1 for end of rectangle
            events.append((x1, y1, y2, 0))
            events.append((x2, y1, y2, 1))
        
        # Sort events by x-coordinate
        events.sort()
        
        # Active y-intervals
        active_y = [0] * len(y_coords)
        current_x = 0
        total_area = 0
        
        for x, y1, y2, event_type in events:
            # Calculate the width of the strip
            width = x - current_x
            
            # Calculate the height of the active y-intervals
            total_height = 0
            for i in range(1, len(active_y)):
                if active_y[i-1] > 0:
                    total_height += y_coords[i] - y_coords[i-1]
            
            # Add the area of the strip to the total area
            total_area = (total_area + width * total_height) % MOD
            
            # Update the current x-coordinate
            current_x = x
            
            # Update the active y-intervals
            if event_type == 0:
                # Rectangle start, activate y-interval
                for i in range(y_index[y1], y_index[y2]):
                    active_y[i] += 1
            else:
                # Rectangle end, deactivate y-interval
                for i in range(y_index[y1], y_index[y2]):
                    active_y[i] -= 1
        
        return total_area

def rectangleArea(rectangles: List[List[int]]) -> int:
    return Solution().rectangleArea(rectangles)