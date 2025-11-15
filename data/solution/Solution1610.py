import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # List to store angles
        angles = []
        # Count of points exactly at the location
        same_points = 0
        
        # Calculate the angle of each point relative to the location
        for x, y in points:
            if x == location[0] and y == location[1]:
                same_points += 1
            else:
                angle_deg = math.degrees(math.atan2(y - location[1], x - location[0]))
                angles.append(angle_deg)
        
        # Sort the angles
        angles.sort()
        # Duplicate the angles to handle the circular nature
        angles.extend([a + 360 for a in angles])
        
        # Initialize the sliding window pointers and the result
        max_visible = 0
        left = 0
        
        # Use a sliding window to find the maximum number of points within the angle
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
        
        # The result is the maximum number of points in the window plus the points at the location
        return max_visible + same_points

def visiblePoints(points: List[List[int]], angle: int, location: List[int]) -> int:
    return Solution().visiblePoints(points, angle, location)