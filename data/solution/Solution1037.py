import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # To determine if three points form a boomerang, we need to check if they are not collinear.
        # Three points (x1, y1), (x2, y2), (x3, y3) are collinear if the area of the triangle they form is zero.
        # The area can be calculated using the determinant method:
        # 0.5 * | x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2) |
        # If the area is zero, the points are collinear, otherwise, they form a boomerang.
        
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # Calculate the determinant (twice the area of the triangle)
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        
        # If the area is not zero, the points are not collinear
        return area != 0

def isBoomerang(points: List[List[int]]) -> bool:
    return Solution().isBoomerang(points)