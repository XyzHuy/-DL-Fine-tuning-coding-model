import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point to the circle within the rectangle
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the distance from the circle's center to this closest point
        distanceX = xCenter - closestX
        distanceY = yCenter - closestY
        
        # If the distance is less than the circle's radius, an intersection occurs
        distanceSquared = distanceX**2 + distanceY**2
        return distanceSquared <= radius**2

def checkOverlap(radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    return Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)