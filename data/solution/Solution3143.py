import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        from collections import defaultdict
        
        # Dictionary to store the maximum x and y coordinates for each tag
        max_coords = defaultdict(lambda: [0, 0])
        
        # Store the points with their tags
        point_tags = [(x, y, tag) for (x, y), tag in zip(points, s)]
        
        # Calculate the maximum x and y coordinates for each tag
        for x, y, tag in point_tags:
            max_coords[tag][0] = max(max_coords[tag][0], abs(x))
            max_coords[tag][1] = max(max_coords[tag][1], abs(y))
        
        # Function to check if a point is inside the square of side length 2*max_side
        def is_inside_square(x, y, max_side):
            return abs(x) <= max_side and abs(y) <= max_side
        
        max_points = 0
        
        # Iterate over each point to consider it as a corner of the square
        for x1, y1, tag1 in point_tags:
            # Calculate the maximum side length that can be formed with this point
            max_side = max(abs(x1), abs(y1))
            
            # Check all points to see how many can be inside the square
            count = 0
            used_tags = set()
            for x2, y2, tag2 in point_tags:
                if is_inside_square(x2, y2, max_side):
                    if tag2 in used_tags:
                        break
                    used_tags.add(tag2)
                    count += 1
            else:
                max_points = max(max_points, count)
        
        return max_points

def maxPointsInsideSquare(points: List[List[int]], s: str) -> int:
    return Solution().maxPointsInsideSquare(points, s)